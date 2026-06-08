import json
import uuid
from pathlib import Path

import pandas as pd
from flask import current_app
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from .extensions import db
from .models import Dataset


def allowed_file(filename: str) -> bool:
    suffix = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
    return suffix in current_app.config["ALLOWED_EXTENSIONS"]


def safe_read_dataframe(path: str) -> pd.DataFrame:
    suffix = Path(path).suffix.lower()
    if suffix == ".csv":
        # low_memory=False improves type inference on mixed columns.
        return pd.read_csv(path, low_memory=False)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    raise ValueError("Unsupported file type.")


def save_uploaded_dataset(file: FileStorage, user_id: int) -> Dataset:
    if not file or not file.filename:
        raise ValueError("No file received.")
    if not allowed_file(file.filename):
        raise ValueError("Only CSV, XLSX, and XLS files are allowed.")

    upload_dir = Path(current_app.config["UPLOAD_DIR"])
    upload_dir.mkdir(parents=True, exist_ok=True)

    original = secure_filename(file.filename)
    suffix = Path(original).suffix.lower()
    stored = f"{uuid.uuid4().hex}{suffix}"
    path = upload_dir / stored
    file.save(path)

    df = safe_read_dataframe(str(path))
    if df.empty:
        path.unlink(missing_ok=True)
        raise ValueError("Dataset is empty.")

    dataset = Dataset(
        user_id=user_id,
        original_filename=original,
        stored_filename=stored,
        file_path=str(path),
        row_count=int(df.shape[0]),
        column_count=int(df.shape[1]),
        columns_json=json.dumps([str(c) for c in df.columns]),
    )
    db.session.add(dataset)
    db.session.commit()
    return dataset

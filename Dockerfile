# Required in production. Generate using: python -c "import secrets; print(secrets.token_urlsafe(48))"
SECRET_KEY=change-this-super-secret-key

# For direct local deploy, SQLite is used by default.
# For PostgreSQL, set something like:
# DATABASE_URL=postgresql://user:password@host:5432/dbname
DATABASE_URL=sqlite:////app/data/app.db

# Where uploaded files and SQLite DB are stored.
DATA_DIR=/app/data
MAX_UPLOAD_MB=50

# Optional real AI insights. If not set, the app uses local rule-based insights.
OPENAI_API_KEY=
OPENAI_MODEL=gpt-4.1-mini

# Server
PORT=10000
FLASK_ENV=production

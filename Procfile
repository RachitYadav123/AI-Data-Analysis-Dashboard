import getpass
import os

from analytics_app import create_app
from analytics_app.extensions import db
from analytics_app.models import User

app = create_app()


@app.cli.command("init-db")
def init_db():
    """Create database tables."""
    with app.app_context():
        db.create_all()
    print("Database initialized.")


@app.cli.command("create-admin")
def create_admin():
    """Create an admin user interactively."""
    email = input("Admin email: ").strip().lower()
    name = input("Admin name: ").strip() or "Admin"
    password = getpass.getpass("Password: ")
    with app.app_context():
        existing = User.query.filter_by(email=email).first()
        if existing:
            print("User already exists.")
            return
        user = User(email=email, name=name, role="admin")
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
    print("Admin created.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "10000")))

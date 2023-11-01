from flask import Flask
from app import db, User
from seed import seed_users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

def create_app():
    with app.app_context():
        db.create_all()
        seed_users()
        print("Database seeded successfully!")

if __name__ == '__main__':
    create_app()
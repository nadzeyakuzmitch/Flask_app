from app import db, User

def seed_users():
    users = ['user1', 'user2', 'user3']  # Seed data
    for username in users:
        new_user = User(username=username)
        db.session.add(new_user)
    db.session.commit()

if __name__ == '__main__':
    seed_users()
    
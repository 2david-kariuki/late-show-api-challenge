from app import db
from models.user import User
from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance
from datetime import date

def seed_data():
    db.drop_all()
    db.create_all()

    # Seed Users
    user = User(username='admin')
    user.set_password('password123')
    db.session.add(user)

    # Seed Guests
    guest1 = Guest(name='John Doe', occupation='Actor')
    guest2 = Guest(name='Jane Smith', occupation='Comedian')
    db.session.add_all([guest1, guest2])

    # Seed Episodes
    episode1 = Episode(date=date(2025, 6, 1), number=1)
    episode2 = Episode(date=date(2025, 6, 2), number=2)
    db.session.add_all([episode1, episode2])

    # Seed Appearances
    appearance1 = Appearance(rating=4, guest_id=1, episode_id=1)
    appearance2 = Appearance(rating=5, guest_id=2, episode_id=2)
    db.session.add_all([appearance1, appearance2])

    db.session.commit()
    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
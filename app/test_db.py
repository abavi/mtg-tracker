from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

# Dependency to get a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add a new user to test the database
def test_create_user():
    # Create a new session
    db: Session = next(get_db())

    # Create a new user
    new_user = User(username="testuser", email="testuser@example.com", hashed_password="hashedpassword123")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    print(f"User created: {new_user.username}, Email: {new_user.email}")

if __name__ == "__main__":
    test_create_user()

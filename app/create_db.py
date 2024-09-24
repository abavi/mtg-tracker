from sqlalchemy.orm import Session
from models import Base
from database import engine

# Create the SQLite database and tables based on the models
print("Creating database...")
Base.metadata.create_all(bind=engine)
print("Database and tables created!")

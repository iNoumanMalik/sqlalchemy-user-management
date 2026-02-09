from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

#creates engine creates a db engine
#sessionmaker → factory for creating sessions
#DeclarativeBase → base class for ORM models

DATABASE_URL = "sqlite:///users.db" # This tells SQLAlchemy which DB to use and where to write content


class Base(DeclarativeBase): # parent class for all ORM models
    pass

# engine: CONNECTS TO THE DATABASE
engine = create_engine( 
    DATABASE_URL,
    echo=True,
)

# session: TALKS TO THE DATABASE
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False) 

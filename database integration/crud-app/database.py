from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create_engine → creates a connection to the database
# declarative_base → used to define database tables using Python classes
# sessionmaker → used to talk to the database (insert, read, update, delete)

SQLALCHEMY_DATABASE_URL="sqlite:///./test.db"
# You are using SQLite database
# The database file name is test.db
# It will be created in the current folder
# If test.db does not exist → SQLAlchemy will create it automatically.

engine=create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False}
)

# engine is the bridge between Python and the database
# check_same_thread=False?
                # SQLite normally allows only one thread
                # Web apps (FastAPI / Flask) use multiple threads
                # This line tells SQLite:“Allow multiple threads to use this database”
                # Without this, your app may crash in web frameworks.
SessionLocal=sessionmaker(bind=engine, autoflush=False, autocommit=False)

# A session is like a temporary workspace->You use it to: Add data, Read data,Update data, Delete data
# bind=engine → session will use this database connection
# autoflush=False → data won’t be sent automatically
# autocommit=False → you must manually call commit()

Base=declarative_base()
# Base is a parent class , Every database table (model) will inherit from this
import os

DB_USER = "root"
DB_PASSWORD = "password"
DB_HOST = "localhost"
DB_NAME = "mydatabase"

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
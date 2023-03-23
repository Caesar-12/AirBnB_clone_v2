#!/usr/bin/python3
"""
Instantiates an object of class FileStorage
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os


st = os.getenv("HBNB_TYPE_STORAGE")
if st == "db":
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()

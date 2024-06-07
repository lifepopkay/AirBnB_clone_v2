#!/usr/bin/python3
"""Instantiates a storage object."""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import Db_storage
    storage = Db_storage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

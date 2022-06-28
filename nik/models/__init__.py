#!/usr/bin/python3
""" adds the storage"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

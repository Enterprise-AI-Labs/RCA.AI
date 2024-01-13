from pymongo import MongoClient
from rca_ai.utils import setup_logger
from typing import LiteralString
import pandas as pd
import tempfile
import os

from rca_ai.constants import APP_ASSETS_DIR



class Handler:
    def __init__(self, name: LiteralString, **kwargs) -> None:
        self.name = name
        pass

    def connect(self, **kwargs):
        pass

    def disconnect(self, **kwargs):
        pass

    def get_dump(self, **kwargs):
        pass


class MongoDBHandler(Handler):
    def __init__(self, name: LiteralString, **kwargs):
        self.name = name
        self.logger = setup_logger(f"mongodb_{kwargs['database']}")
        self.host = kwargs["host"]
        self.port = kwargs["port"]
        self.username = kwargs["username"]
        self.password = kwargs["password"]
        self.database = kwargs["database"]
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.host, self.port, username=self.username, password=self.password)
            self.db = self.client[self.database]
            self.logger.debug("connected to MongoDB")
        except Exception as e:
            self.logger.error(f"failed to connect to MongoDB for db {self.database}: {e}")

    def disconnect(self):
        try:
            if self.client:
                self.client.close()
                self.logger.debug("disconnected from MongoDB")
        except Exception as e:
            self.logger.error(f"failed to disconnect from MongoDB for db {self.database}: {e}")

    def get_dump(self, **kwargs):
        try:
            columns = kwargs["columns"]
            collection = self.db[kwargs["collection"]]
            projection = {col: 1 for col in columns} if columns else None
            result = collection.find({}, projection)
            df = pd.DataFrame(list(result))
            if APP_ASSETS_DIR == "":
                self.logger.error(f"assets directory is empty {APP_ASSETS_DIR}")
                exit(1)
            dump_path = os.path.join(APP_ASSETS_DIR, f"{self.name}")
            df.to_parquet(dump_path, compression='gzip')
            return dump_path
        except Exception as e:
            self.logger.error(f"failed to get dump from mongodb for db {self.database}: {e}")
            return []

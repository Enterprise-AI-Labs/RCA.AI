from typing import List, LiteralString
from .handlers import *
from rca_ai.utils import *
import pandas as pd

class DBIndex:
    def __init__(self, handlers: List[Handler]) -> None:
        self.dumps = {}
        # TODO: parallelize this code
        for handler in handlers:
            handler.connect()
            self.dumps[handler.name] = handler.get_dump()
            handler.disconnect()
    
    def get_log_file_candidates(self, log_bundle: LiteralString):
        filepaths = get_filepaths(directory=log_bundle)
        log_file_candidates = []
        for _, dump in self.dumps:
            df = pd.read_parquet(dump)
            for keyword in df["keywords"]:
                for fp in filepaths:
                    if keyword in fp:
                        log_file_candidates.append(fp)
        


        


        


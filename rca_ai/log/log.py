from typing import LiteralString, List
from rca_ai.utils import read_file_lines
import os

class LogContent:
    def __init__(self, log_file: LiteralString) -> None:
        self.unstructured = read_file_lines(filepath=log_file)
        # TODO: use log parser
        self.structured = None

class LogSignature:
    def __init__(self, log_filepath: LiteralString) -> None:
        self.sign = None

class Log:
    def __init__(self, log_filepath: LiteralString) -> None:
        self.filename: LiteralString = log_filepath
        self.matched_keywords_filename: List[LiteralString] = []
        self.log_content: LogContent = None
        self.matched_signatures: List[LogSignature] = []


    

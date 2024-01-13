import json
import  yaml
from typing import LiteralString, Dict, Union, List
import os
import glob

def get_filepaths(directory: LiteralString) -> List[LiteralString]:
    """Get filepaths of different log files

    Args:
        directory (LiteralString): directory containing log files

    Returns:
        List[LiteralString]: list of filepaths
    """
    pattern = os.path.join(directory, '**', '*.*')
    for fp in glob.glob(pattern, recursive=True):
        yield fp

def read_file_lines(filepath: LiteralString):
    return open(filepath, "r").readlines()
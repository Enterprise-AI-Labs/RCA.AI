import re
from typing import List
from rca_ai.log import Log, LogSignature
from rca_ai.db import DBIndex
from rca_ai.utils import read_file_lines

def perform_pattern_matching(db_index: DBIndex, log_bundle: str) -> List[Log]:
    filepath_signature_mapping = db_index.get_filepath_signature_mapping(log_bundle)
    
    logs = []
    
    for filepath, signatures in filepath_signature_mapping.items():
        try:
            file_content = ' '.join(read_file_lines(filepath))
        except IOError as e:
            print(f"Error reading file {filepath}: {e}")
            continue  
        
        log = Log(log_filepath=filepath)
        
        for signature in signatures:
            try:
                pattern = re.compile(signature)
                match = pattern.search(file_content)
                if match:
                    log_signature = LogSignature(log_filepath=filepath)
                    log_signature.sign = signature
                    log.matched_signatures.append(log_signature)
            except re.error as e:
                print(f"Regex error with pattern {signature}: {e}")
                continue
        
        logs.append(log)
    
    return logs

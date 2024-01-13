import argparse
import tempfile
from .constants import APP_ASSETS_DIR

class RCA:
    def __init__(self) -> None:
        pass


def main():
    global APP_ASSETS_DIR
    APP_ASSETS_DIR = tempfile.mkdtemp(prefix="rca_ai_app_assets")
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('directory', help='The directory to search for files.')
    parser.add_argument('keyword', help='The keyword to search for in filenames.')
    args = parser.parse_args()

if __name__ == "__main__":
    main()
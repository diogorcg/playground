from pathlib import Path

BASE_DIR = Path(__file__).parent.parent.absolute()

CREDENTIALS_DIR = Path(BASE_DIR, "credentials")
DATA_DIR = Path(BASE_DIR, "data")
DOCS_DIR = Path(BASE_DIR, "docs")
MODELS_DIR = Path(BASE_DIR, "models")
NOTEBOOKS_DIR = Path(BASE_DIR, "notebooks")
QUERIES_DIR = Path(BASE_DIR, "queries")
TESTS_DIR = Path(BASE_DIR, "tests")

# create dirs
BASE_DIR.mkdir(parents=True, exist_ok=True)
CREDENTIALS_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)
DOCS_DIR.mkdir(parents=True, exist_ok=True)
MODELS_DIR.mkdir(parents=True, exist_ok=True)
NOTEBOOKS_DIR.mkdir(parents=True, exist_ok=True)
QUERIES_DIR.mkdir(parents=True, exist_ok=True)
TESTS_DIR.mkdir(parents=True, exist_ok=True)

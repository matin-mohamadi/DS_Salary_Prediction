from pathlib import Path

PROJECT_ROOT = next(
    parent for parent in Path(__file__).resolve().parents
    if (parent/"pyproject.toml").is_file()
)

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"

DATASET_PATH = RAW_DATA_DIR / "DataScience_salaries_2024.csv"
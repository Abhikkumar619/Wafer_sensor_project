from pathlib import Path
from dataclasses import dataclass




@dataclass(frozen=True)
class DataIngestionConfig: 
    root_dir: Path
    data_source: Path
    data_source: Path
    train_data_path: Path
    test_data_path: Path
    data_to_store: Path
    
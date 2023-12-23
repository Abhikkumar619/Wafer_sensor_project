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
    
@dataclass(frozen=True)
class DataTransformationConfig: 
    root_dir: Path
    preprocessor_obj_file: Path
    train_data_path: Path
    test_data_path: Path
    scaled_train_data: Path
    scaled_test_data: Path
    
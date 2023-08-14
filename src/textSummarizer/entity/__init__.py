from dataclasses import dataclass
from pathlib import Path

#its a data class where one can mention their variables
# pull variables from config.yaml and type in the data types
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


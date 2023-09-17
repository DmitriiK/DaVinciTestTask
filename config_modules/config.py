from pydantic import BaseModel  # , validator
from enum import Enum
from typing import Dict, List
from config_modules.metadata_classes import EntityTypes


class CompressionTypes(str, Enum):
    snappy = "snappy"
    gzip = 'gzip'


class ConfigET(BaseModel):
    """entity type specific section of configFile"""
    metadata_file: str
    source_data_file: str


class Config(BaseModel):
    """kind of data class for application configuration"""
    input_dir: str = 'input_data'
    output_dir: str = "output_data"
    metadata_dir: str = 'metadata'  
    """chunk size to write to parquet big dataframe"""
    chunk_size: int
    compression: CompressionTypes = CompressionTypes.snappy
    partitioning_columns: List[str] = []
    entity_type_configs: Dict[EntityTypes, ConfigET]

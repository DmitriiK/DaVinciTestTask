from pydantic import BaseModel  # , validator
from typing import Dict
from config_modules.metadata_classes import EntityTypes


class ConfigET(BaseModel):
    """entity type specific section of configFile"""
    metadata_file: str
    source_data_file: str


class Config(BaseModel):
    """kind of data class for application configuration"""
    input_dir: str = 'input_data'
    output_dir: str = "output_data"
    metadata_dir: str = 'metadata'
    entity_type_configs: Dict[EntityTypes, ConfigET]

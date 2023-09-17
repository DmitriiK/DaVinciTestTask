
import os
from pydantic_yaml import parse_yaml_raw_as

from config_modules.config import Config
from config_modules.metadata_classes import PandasSchema, EntityTypes

CONFIG_FILE_PATH = 'config.yml'


class ConfigReader:
    """responsible for loading of data from main config files 
    and for loading of metadata for different entity types
    references to metadata files supposed to be taken from main config file"""
    def __init__(self):
        conf = ConfigReader.__parse_from_yaml_file(CONFIG_FILE_PATH, Config)
        self.application_config = conf

    @staticmethod
    def __parse_from_yaml_file(file_path: str, pydantic_class_name):
        with open(file_path, 'r') as file:
            yml = file.read()
            ps = parse_yaml_raw_as(pydantic_class_name, yml)
            return ps

    def get_pandas_schema(self, et: EntityTypes) -> PandasSchema:
        conf = self.application_config
        md_path = conf.entity_type_configs[et].metadata_file
        file_path = os.path.join(conf.metadata_dir, md_path)
        ps = ConfigReader.__parse_from_yaml_file(file_path, PandasSchema)
        return ps

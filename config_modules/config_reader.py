
import os
from pydantic_yaml import parse_yaml_raw_as

from config_modules.config import Config
from config_modules.metadata_classes import PandasSchema, EntityTypes

CONFIG_FILE_PATH = 'config.yml'


class ConfigReader:
    def __init__(self):
        conf = ConfigReader.parse_from_yaml_file(CONFIG_FILE_PATH, Config)
        self.application_config = conf

    @staticmethod
    def parse_from_yaml_file(file_path: str, pydantic_class_name): 
        with open(file_path, 'r') as file:
            yml = file.read()
            ps = parse_yaml_raw_as(pydantic_class_name, yml)
            return ps

    def get_pandas_schema(self, et: EntityTypes) -> PandasSchema:
        conf = self.application_config
        md_path = ''
        match et:
            case EntityTypes.order:
                md_path = conf.orders_metadata_file
            case EntityTypes.order_item:
                md_path = conf.order_items_metadata_file
            case EntityTypes.order_payment:
                md_path = conf.order_payments_metadata_file
            case EntityTypes.product:
                md_path = conf.products_metadata_file_file                                     
            case _:
                raise Exception(f'Sorry, we don''t know about {et} entity')

        file_path = os.path.join(conf.metadata_dir, md_path)
        ps = ConfigReader.parse_from_yaml_file(file_path, PandasSchema)
        return ps
    

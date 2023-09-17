from pydantic import BaseModel  # , validator
from pydantic_yaml import to_yaml_str


class config(BaseModel):
    input_dir: str = 'input_data'
    output_dir: str = "output_data"
    metadata_dir: str = 'metadata'
    orders_data_file: str = 'olist_orders_dataset.csv'
    order_items_data_file: str = 'olist_order_items_dataset.csv'


if __name__ == "__main__":
    print('manual dev testing of config classes')
    m1 = config()
    # This dumps to YAML
    yml = to_yaml_str(m1)
    print(yml)

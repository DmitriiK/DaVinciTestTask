from pydantic import BaseModel  # , validator


class Config(BaseModel):
    input_dir: str = 'input_data'
    output_dir: str = "output_data"
    metadata_dir: str = 'metadata'
    orders_metadata_file: str
    order_items_metadata_file: str
    products_metadata_file: str
    order_payments_metadata_file: str

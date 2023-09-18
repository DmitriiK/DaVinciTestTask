from enum import Enum
from pydantic import BaseModel  # , validator
"""
    Data Classes for information about metadata, related to source files
    Structures of the classes reflected in correspondent yaml files
    for configurations
"""


class PandasDataType(str, Enum):
    object = "object"
    int = 'int'
    uint8 = 'uint8'
    float = 'float'
    float32 = 'float32'
    date_time = "datetime64"
    bool = 'bool'
    category = 'category'


class PandasColumn(BaseModel):
    column_name: str
    dtype: PandasDataType = PandasDataType.object
    is_in_index: bool = False


class PandasSchema(BaseModel):
    entity_name: str
    columns: list[PandasColumn]


class EntityTypes(str, Enum):
    order = "order"
    order_item = 'order_item'
    order_payment = 'order_payment'
    product = 'product'

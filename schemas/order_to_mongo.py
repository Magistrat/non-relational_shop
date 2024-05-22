from typing import List

from pydantic import BaseModel
from pydantic import Field

from schemas import ItemSchema


class OrderToMongo(BaseModel):
    """
    Схема заказа в интернете магазине (с товарами)
    """
    username: str = Field(
        description='Имя пользователя',
        init_var=True,
        kw_only=True,
        default='Bob'
    )
    phone: str = Field(
        description='Телефон',
        init_var=True,
        kw_only=True,
        default='88005553535'
    )
    address: str = Field(
        description='Адрес',
        init_var=True,
        kw_only=True,
        default=''
    )
    products: List[ItemSchema] = Field(
        description='Товары в заказе',
        init_var=True,
        kw_only=True,
        default=[]
    )

    class Config:
        json_schema_extra = {
            "properties": {
                "username": {
                    "type": "string",
                    "nullable": False,
                    "description": "Имя пользователя",
                    "example": "Bob",
                },
                "phone": {
                    "type": "string",
                    "nullable": False,
                    "description": "Телефон",
                    "example": "88005553535",
                },
                "address": {
                    "type": "string",
                    "nullable": False,
                    "description": "Адрес"
                },
                "products": {
                    "type": "array",
                    "items": ItemSchema.Config.json_schema_extra,
                    "description": "Товары в заказе",
                }
            }
        }

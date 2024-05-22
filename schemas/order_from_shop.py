from typing import List

from pydantic import BaseModel
from pydantic import Field


class OrderFromShop(BaseModel):
    """
    Схема заказа в интернете магазине (с id товарами)
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
    products: List[str]
    # products: List[str] = Field(
    #     description='Список _id записей в Mongo',
    #     init_var=True,
    #     kw_only=True
    # )

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
                    # "type": "array",
                    "nullable": False,
                    "description": "Список _id записей в Mongo",
                }
            }
        }

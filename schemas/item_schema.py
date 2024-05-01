from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class ItemSchema(BaseModel):
    """
    Схема товара в интернет магазине
    """
    itemName: Optional[str] = Field(
        description='Название товара',
        init_var=True,
        kw_only=True
    )
    description: Optional[str] = Field(
        description='Описание товара',
        init_var=True,
        kw_only=True
    )
    measure: Optional[str] = Field(
        description='Единица измерения',
        init_var=True,
        kw_only=True,
        default='шт.'
    )
    price: Optional[float] = Field(
        description='Цена товара за у.е.',
        init_var=True,
        kw_only=True,
        decimal_places=2,
        gt=0
    )
    photo_url: Optional[str] = Field(
        description='URL-ссылка фотографии',
        init_var=True,
        kw_only=True,
    )

    class Config:
        json_schema_extra = {
            "properties": {
                "itemName": {
                    "type": "string",
                    "nullable": True,
                    "description": "Название товара"
                },
                "description": {
                    "type": "string",
                    "nullable": True,
                    "description": "Описание товара"
                },
                "measure": {
                    "type": "string",
                    "nullable": True,
                    "description": "Единица измерения",
                    "example": "шт.",
                },
                "price": {
                    "type": "float",
                    "nullable": True,
                    "description": "Цена товара за у.е.",
                    "example": 100.00,
                },
                "photo_url": {
                    "type": "string",
                    "nullable": True,
                    "description": "URL-ссылка фотографии",
                    "example": "https://example.org/photos/cake.jpg",
                },
            }
        }

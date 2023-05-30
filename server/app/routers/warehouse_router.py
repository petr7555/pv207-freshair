from typing import TypedDict

from fastapi import APIRouter

router = APIRouter(
    prefix="/warehouse",
    tags=["warehouse"],
)


class Item(TypedDict):
    name: str
    quantity: int


class WarehouseStatus(TypedDict):
    items: list[Item]


@router.get("/")
def get_warehouse_status() -> WarehouseStatus:
    mock_data: WarehouseStatus = {
        "items": [
            {"name": "fan", "quantity": 50},
            {"name": "cable", "quantity": 200},
            {"name": "casing", "quantity": 10}
        ]
    }
    return mock_data

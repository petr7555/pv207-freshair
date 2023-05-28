from typing import TypedDict

from fastapi import APIRouter

router = APIRouter(
    prefix="/finance",
    tags=["finance"],
)


class Sale(TypedDict):
    date: str
    amount: int


class FinanceData(TypedDict):
    sales: list[Sale]


@router.get("/")
def get_finance_data() -> FinanceData:
    mock_data: FinanceData = {
        "sales": [
            {"date": "2021-01-01", "amount": 100},
            {"date": "2021-01-02", "amount": 200},
        ]
    }
    return mock_data

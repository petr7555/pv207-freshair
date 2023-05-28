from typing import TypedDict

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/dac",
    tags=["dac"],
)


class DacSolution(TypedDict):
    id: str
    customerName: str
    customerEmail: str
    metricsUrl: str


@router.get("/")
def get_deployed_dac_solutions() -> list[DacSolution]:
    mock_data: list[DacSolution] = [
        {
            "id": "1",
            "customerName": "Car factory",
            "customerEmail": "jbpm.pv207@gmail.com",
            "metricsUrl": "http://127.0.0.1:8000/dac/1/metrics",
        },
        {
            "id": "2",
            "customerName": "Conscious village",
            "customerEmail": "jbpm.pv207@gmail.com",
            "metricsUrl": "http://127.0.0.1:8000/dac/2/metrics",
        },
    ]

    return mock_data


class DacMetrics(TypedDict):
    cpuUsage: int
    temperature: int
    backupBatteryLife: int


@router.get("/{dac_id}/metrics")
def get_dac_metrics(dac_id: str) -> DacMetrics:
    mock_data: dict[str, DacMetrics] = {
        "1": {
            "cpuUsage": 50,
            "temperature": 30,
            "backupBatteryLife": 90,
        },
        "2": {
            "cpuUsage": 90,
            "temperature": 50,
            "backupBatteryLife": 95,
        },
    }

    dac_metric = mock_data.get(dac_id)

    if dac_metric is None:
        raise HTTPException(404, f"DAC with id {dac_id} not found")

    return dac_metric

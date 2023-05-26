from typing import TypedDict

from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/dac",
    tags=["dac"],
)


class DacSolution(TypedDict):
    id: str
    metricsUrl: str


@router.get("/")
def get_deployed_dac_solutions() -> list[DacSolution]:
    mock_data: list[DacSolution] = [
        {"id": "1",
         "metricsUrl": "http://127.0.0.1:8000/dac/1/metrics"},
        {"id": "2",
         "metricsUrl": "http://127.0.0.1:8000/dac/2/metrics"},
    ]

    return mock_data


class DacMetric(TypedDict):
    cpuUsage: int
    memoryUsage: int
    storageUsage: int
    temperature: int
    batteryLife: int


@router.get("/{dac_id}/metrics")
def get_dac_metrics(dac_id: str) -> DacMetric:
    mock_data: dict[str, DacMetric] = {
        "1": {
            "cpuUsage": 50,
            "memoryUsage": 50,
            "storageUsage": 50,
            "temperature": 50,
            "batteryLife": 50,
        },
        "2": {
            "cpuUsage": 100,
            "memoryUsage": 100,
            "storageUsage": 100,
            "temperature": 100,
            "batteryLife": 100,
        }
    }

    dac_metric = mock_data.get(dac_id)

    if dac_metric is None:
        raise HTTPException(404, f"DAC with id {dac_id} not found")

    return dac_metric

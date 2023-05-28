from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routers import dac_router, finance_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dac_router.router)
app.include_router(finance_router.router)


@app.get("/")
@app.get("/health")
def health_check() -> str:
    return "Server OK"

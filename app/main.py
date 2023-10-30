from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.config import settings
from app.routers import item

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(item.router, prefix=settings.API_V1_STR)


@app.get("/")
def root():
    return {"HELLO": "THERE"}

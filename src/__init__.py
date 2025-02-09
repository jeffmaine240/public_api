from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.retrieval_app.routes import retrieve_router


version = "v1"

@asynccontextmanager
async def life_span(app:FastAPI):
    print("server is starting ...")
    yield
    print("server has been stopped.")


app = FastAPI(
    title="Public Api",
    description="A public api to retrieve basic information",
    version=version,
    lifespan= life_span,
)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)


app.include_router(retrieve_router, prefix=f"/api/{version}/public", tags=["public"])




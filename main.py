from fastapi import FastAPI
from routes.routeScraping import routeScraping

app = FastAPI()

app.include_router(routeScraping)

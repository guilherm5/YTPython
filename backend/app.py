from fastapi import FastAPI
from routes.routes_download import router 

app = FastAPI()
app.include_router(router)
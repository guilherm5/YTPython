from fastapi import FastAPI
from routes.download_thumbnail import router 

app = FastAPI()
app.include_router(router)
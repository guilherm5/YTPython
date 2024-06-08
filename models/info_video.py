from pydantic import BaseModel

class Video(BaseModel): 
    url_video: str | None = None
    #titulo_video: str | None = None
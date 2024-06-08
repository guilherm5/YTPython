from pydantic import BaseModel

class Video(BaseModel): 
    url_video: str | None = None
    acao_midia: str | None = None
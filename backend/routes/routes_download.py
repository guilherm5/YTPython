from fastapi import APIRouter
from controller.controller_download import download_thumbnail, download_midia_youtube
from models.info_video import Video

router = APIRouter()

@router.post("/download_thumbnail")
async def thumbnail_download(video_obj: Video):
    return await download_thumbnail(video_obj=video_obj)

@router.post("/download_midia_youtube")
async def download_video(video_obj: Video):
    return await download_midia_youtube(video_obj=video_obj)

@router.get("/hello")
async def hello():
    return {"hello": "user"}

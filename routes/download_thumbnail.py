from fastapi import APIRouter
from controller.download_thumbnail import download_thumbnail
from models.info_video import Video

router = APIRouter()

@router.post("/download_thumbnail/")
async def read_users(video_obj: Video):
    return await download_thumbnail(video_obj=video_obj)


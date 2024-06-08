from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import urllib.request
import os
from models.info_video import Video

async def download_thumbnail(video_obj: Video):  
    try:
        yt = YouTube(video_obj.url_video)
        thumb = yt.thumbnail_url
        
        # Obtendo o diretório de download padrão do sistema operacional
        download_directory = os.path.expanduser("~/downloads")
        image_path = os.path.join(download_directory, yt.title + ".jpg")
        urllib.request.urlretrieve(thumb, image_path)
        return {"thumb": thumb, "Vídeo": yt.title}
    except VideoUnavailable:
        print(f"Video {yt} indisponível.")
        return(f"Video {yt} indisponível.")
    except Exception as err:
        print(f"Erro ao realizar download da thumbnail, erro: {err}")
        return f"Erro ao realizar download da thumbnail, erro: {err}"

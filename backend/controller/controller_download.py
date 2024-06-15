from pytube import YouTube
from pytube.exceptions import VideoUnavailable
import urllib.request
import os
from models.info_video import Video
import re

DOWNLOAD_DIR = os.path.expanduser("~/downloads")


def clean_filename(filename):
    cleaned_filename = re.sub(r'[\\/*?:"<>|]', '_', filename)
    return cleaned_filename

# Função para definir path e diretorio de download da thumbnail
def download_file_path(url_video: str, filename: str, ext: str) -> str:
    path = os.path.join( clean_filename(filename) + ext) # Funcao clean_filename limpa o nome do video baixado, para nao ocorrer erros no windows
    urllib.request.urlretrieve(url_video, path)
    return path

# Download thumbnail youtube
async def download_thumbnail(video_obj: Video):
    try:
        yt = YouTube(video_obj.url_video)
        thumbnail_path = download_file_path(yt.thumbnail_url, yt.title, ".jpg")
        
        return {"thumb": thumbnail_path, "Vídeo": yt.title}
    except VideoUnavailable:
        print(f"Vídeo {yt} indisponível.")
        return(f"Vídeo {yt} indisponível.")
    except Exception as err:
        print(f"Erro ao realizar download da thumbnail, erro: {err}")
        return f"Erro ao realizar download da thumbnail, erro: {err}"

# Download audio e video youtube
async def download_midia_youtube(video_obj: Video):
    try:
        yt = YouTube(video_obj.url_video)
        data = None

        if video_obj.acao_midia == 'download_video':
            data = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        elif video_obj.acao_midia == 'download_audio':
            data = yt.streams.filter(only_audio=True).first()
        data.download(output_path = DOWNLOAD_DIR, filename=clean_filename(yt.title) + ".mp3")
        
        return {"mensagem": f"download: {data.title}"}
    except VideoUnavailable as v_error:
        print(f"Áudio {yt.title} indisponível, erro: {v_error}")
        return f"Áudio {yt.title} indisponível, erro: {v_error}"
    except Exception as err:
        print(f"Erro ao realizar download do áudio {yt.title}, erro: {err}")
        return f"Erro ao realizar download do áudio {yt.title}, erro: {err}"
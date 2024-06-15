async function download_midia() {
    // Tratar overlay de carragamento
    document.getElementById("loading-overlay").style.display = "block";

    const linkVideo = document.getElementById("link-youtube").value;
    const bodyVideo = JSON.stringify({
        "url_video": linkVideo,
        "acao_midia": "download_video"
    });

    const headersVideo = new Headers();
    headersVideo.append("Content-Type", "application/json");
  
    try{
        const response = await fetch("http://127.0.0.1:8000/download_midia_youtube",{
            method: "POST",
            body: bodyVideo,
            headers: headersVideo
        })
    }catch(error){
        console.log("Erro na requisição fetch: ", error.message)
    }finally{
        /*tratar finally*/ 
    }
        
    
}
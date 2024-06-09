async function download_thumbnail() {
    var linkDoVideo = document.getElementById("link-youtube").value;
    const body = JSON.stringify({
        "url_video": linkDoVideo
    });
    /* Definindo parametros para servidor fetch */ 
    const header = {"Content-Type": "application/json"}
    const requestOptions = {
        method: "POST",
        headers: header,
        body: body
    };

    fetch("http://127.0.0.1:8000/download_thumbnail/", requestOptions)
    .then((response) => response.text())
    .then((result) => console.log(result))
    .catch((error) => console.error(error));
}



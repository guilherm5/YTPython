async function download_midia() {
    let acaoVideo = ""; 
    const enderecoAtual = window.location.href;
    if (enderecoAtual === 'http://127.0.0.1:5500/frontend/index.html?') {
        acaoVideo = 'download_video';
    } else if (enderecoAtual === 'http://127.0.0.1:5500/frontend/music.html?') {
        acaoVideo = 'download_audio';
    } else {
        console.log('Nenhuma condição correspondeu à URL atual:', enderecoAtual);
    }

    // Mostra overlay de carregamento
    document.getElementById("loading-overlay").style.display = "block";

    const linkVideo = document.getElementById("link-youtube").value;
    const bodyVideo = JSON.stringify({
        "url_video": linkVideo,
        "acao_midia": acaoVideo
    });

    const headersVideo = new Headers();
    headersVideo.append("Content-Type", "application/json");
    
    try {
        const response = await fetch("http://127.0.0.1:8000/download_midia_youtube", {
            method: "POST",
            body: bodyVideo,
            headers: headersVideo
        });
        const result = await response.text();
        console.log("resultado", result);
        
    } catch (error) {
        console.error("erro fetch", error);
    } finally {
        document.getElementById("loading-overlay").style.display = "none";
    }
}
const btnDownload = document.getElementById('btn-download');
// Adiciona um event listener para o evento de clique
btnDownload.addEventListener('click', function(event) {
    // Previne o comportamento padrão do botão (no caso de estar dentro de um formulário)
    event.preventDefault();
    download_midia();
});

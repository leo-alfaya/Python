window.onload = function() {
	// Normaliza as várias versões de getUserMedia de acordo com os fabricantes.
	navigator.getUserMedia = (navigator.getUserMedia ||
		navigator.webkitGetUserMedia ||
		navigator.mozGetUserMedia ||
		navigator.msGetUserMedia);

	// Checa se o browser suporta getUserMedia.
	// Caso não, mostra um alert, senão continua.
	if (navigator.getUserMedia) {
		// Requesita a câmera.
		navigator.getUserMedia(
		// Constraints
		{
			video: true
		},
	
		// Função de Callback de Sucesso
		function(localMediaStream) {
			camera_stream = document.getElementById("camera-stream");
			camera_stream.src = window.URL.createObjectURL(localMediaStream);
		},
		
		// Função de Callback de Erro
		function(err) {
			// Loga o erro no console.
			console.log('O erro aconteceu quando tentamos acessar getUserMedia: ' + err);
		});

	} else {
		alert('Desculpe, seu browser não suporta getUserMedia');
	}
}
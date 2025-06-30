let img = document.querySelector('.container-cine-home');
let imagemUrl = "{{imagem_url}}";  // Variável Jinja sendo passada para o JavaScript
img.style.backgroundImage = 'linear-gradient(#000000, #00000000, #141414), url(' + imagemUrl + ')';

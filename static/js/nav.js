
window.addEventListener("scroll", function () {
    let nav = document.querySelector('.fixar');
    
    // Verifica o tamanho da tela
    let scrollThreshold = (window.innerWidth <= 768) ? 50 : 100;  // 50 para celular, 100 para telas maiores
    
    if (window.scrollY > scrollThreshold) {
      nav.classList.add('nav-cor');
    } else {
      nav.classList.remove('nav-cor'); // Cor original
    }
  });
function setActiveNavButton() {
    const pagina = window.location.pathname; // Obtém o caminho da URL atual
    const inicio = document.getElementById('inicio');
    const series = document.getElementById('series');
    const filmes = document.getElementById('filmes');
    const infantil = document.getElementById('infantil');
    const lista = document.getElementById('lista');


    

   
        if( pagina == "/inicio" ){
            inicio.style.color = '#fff'
        } 
        else if( pagina == "/filmes"){
            filmes.style.color = '#fff'

        }
        else if( pagina == "/series"){
            series.style.color = '#fff'

        }
        else if( pagina == "/infantil"){
            infantil.style.color = '#fff'

        }
        else if( pagina == "/Minha-lista"){
            lista.style.color = '#fff'

        }
}

// Executa a função quando a página carrega
window.addEventListener('load', setActiveNavButton);
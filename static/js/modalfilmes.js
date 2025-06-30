// Seleção dos elementos
const modalOverlay = document.querySelector('.modal-overlay');
const closeButton = document.querySelector('.close-btn');

// Função para abrir o modal
function openModal(trailer, titulo, descricao, tamanho, tipo, data, imgfundo, genero1, genero2, genero3, genero4, genero5, lista, curtida, idmidia) {
  document.getElementById('titulo').innerText = titulo;
  document.getElementById('ano').innerText = 'Lançamento: ' + data;
  if (tipo == 'movie') {
    const horas = Math.floor(tamanho / 60);
    const minutos = tamanho % 60;
    document.getElementById('tamanhos').innerText = 'Duração: ' + horas + 'h' + minutos + 'min';

  } else {
    document.getElementById('tamanhos').innerText = 'Temporadas: ' + tamanho;
  }
  const trailer_html = `
  <iframe 
    id="trailer" 
    src="${trailer}" 
    title="Video"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
    allowfullscreen>
  </iframe>
`;
  const img_html = `<img src="${imgfundo}" alt="">`
  if (trailer == "None" || trailer == null) {
    document.getElementById('trailer_img').innerHTML = img_html

  } else {
    document.getElementById('trailer_img').innerHTML = trailer_html

  }
  let curtida_html;
  if (curtida=='sim'){
     curtida_html = `
        <button class="like-btn" onclick="descurtir(this, '${idmidia}')"><i class="fa-solid fa-thumbs-up"></i>  Descurtir</button>`;
      }
  else{
     curtida_html = `
        <button class="like-btn" onclick="curtir(this, '${idmidia}')"><i class="fa-regular fa-thumbs-up"></i>  Curtir</button>`;
      }

  let lista_html;
  if (lista =='sim'){
   lista_html = `
            <button class="add-btn"  onclick="toggleListaRemover(this, '${idmidia}')"><i class="fa-solid fa-check"></i> Remover da lista</button>

  `;
  }else{
    lista_html = `
    <button class="add-btn"  onclick="toggleLista(this, '${idmidia}')"><i class="fa-solid fa-plus"></i>  Adicionar à lista</button>

`;
    
  }
  let generos = [genero1, genero2, genero3, genero4, genero5];
  let generosFiltrados = generos.filter(g => g !== "");
  document.getElementById('gen').innerText = 'Genero: ' + generosFiltrados.join(' , '); document.getElementById('desc').innerText = descricao;


  buttons = document.querySelector('.action-buttons').innerHTML = curtida_html + lista_html







  modalOverlay.classList.add('active');
}

// Fechar o modal ao clicar no botão
closeButton.addEventListener('click', () => {
  modalOverlay.classList.remove('active');
});

// Fechar o modal ao clicar fora
modalOverlay.addEventListener('click', (e) => {
  if (e.target === modalOverlay) {
    modalOverlay.classList.remove('active');
  }
});

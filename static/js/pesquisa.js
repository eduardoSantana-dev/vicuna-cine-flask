let valorinput = document.getElementById("meuInput");
console.log(valorinput);

document.addEventListener("DOMContentLoaded", function () {
    let inputField = document.getElementById("meuInput");
    let resultadoDiv = document.getElementById("resultados"); // Criar uma div no HTML para os resultados
    let timeout;

    inputField.addEventListener("input", function () {
        clearTimeout(timeout); // Limpa o timeout anterior se houver
        let home = document.getElementById('home');
        if (inputField.value.length > 1) { 
            // Define o delay (500ms)
            timeout = setTimeout(function() {
                home.style.display = 'none';
                enviarParaFlask(inputField.value);
                atualizarTituloPesquisa(inputField.value); // Atualiza o título com o texto digitado
            }, 500); // O delay é de 500ms após o último caractere digitado
        } else {
            home.style.display = 'block';
            resultadoDiv.innerHTML = ""; // Limpa os resultados se o input estiver vazio
            atualizarTituloPesquisa(""); // Limpa o título se o input estiver vazio
        }
    });
});

function atualizarTituloPesquisa(texto) {
    let titulo = document.getElementById("titulo-pesquisa");
    
    // Se o título não existir, cria o título
    if (!titulo) {
        titulo = document.createElement('h2');
        titulo.id = 'titulo-pesquisa';
    }

    // Atualiza o texto do título com o que o usuário digitou
    titulo.textContent = texto ? `Você está buscando por: ${texto}` : "Digite sua pesquisa...";
}

function enviarParaFlask(valor) {
    fetch("/processar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ texto: valor })
    })
    .then(response => response.json())
    .then(data => {
        mostrarResultados(data.resposta, valor); // Passa o valor do input como parâmetro
    })
    .catch(error => console.error("Erro:", error));
}

function mostrarResultados(resultados, valor) {
    let titulo = document.getElementById('titulo-pesquisa');
    let resultadoDiv = document.getElementById("resultados");
    resultadoDiv.innerHTML = ""; // Limpa os resultados anteriores

    timeout = setTimeout(function() {
        titulo.style.display = 'block';
        let container = document.createElement("div");
        container.className = "container-fluid cont-cards";

        let row = document.createElement("div");
        row.className = "row g-4";

        resultados.forEach(midia => {
            let col = document.createElement("div");
            col.className = "col-auto";

            let card = document.createElement("div");
            card.className = "card cardmidia";

            let imgDiv = document.createElement("div");
            imgDiv.className = "img";
            imgDiv.onclick = function() {
                openModal(midia.trailer, midia.nome, midia.descricao, midia.tamanho, midia.tipo, midia.lancamento, midia.imgfundo, ...midia.genero.slice(1, 6));
            };

            let img = document.createElement("img");
            img.src = midia.poster;
            img.alt = "";

            imgDiv.appendChild(img);
            card.appendChild(imgDiv);

            let detalhes = document.createElement("div");
            detalhes.className = "detalhes";

            let tituloMidia = document.createElement("div");
            tituloMidia.className = "titulo-midia";
            tituloMidia.onclick = function() {
                openModal(midia.trailer, midia.nome, midia.descricao, midia.tamanho, midia.tipo, midia.lancamento, midia.imgfundo, ...midia.genero.slice(1, 6));
            };

            let tituloMidiaP = document.createElement("p");
            tituloMidiaP.className = "titulo-midiap";
            tituloMidiaP.textContent = midia.nome;

            let tamanhoMidia = document.createElement("p");
            tamanhoMidia.className = "tamanho-midia";

            if (midia.tipo === 'movie') {
                let horas = Math.floor(midia.tamanho / 60);
                let minutos = midia.tamanho % 60;
                tamanhoMidia.textContent = horas > 0 ? `${horas}h ${minutos}min` : `${minutos}min`;
            } else {
                tamanhoMidia.textContent = midia.tamanho > 1 ? `${midia.tamanho} temporadas` : `${midia.tamanho} temporada`;
            }

            tituloMidia.appendChild(tituloMidiaP);
            tituloMidia.appendChild(tamanhoMidia);
            detalhes.appendChild(tituloMidia);

            let botoesMidia = document.createElement("div");
            botoesMidia.className = "botoes-midia";

            let inputHidden = document.createElement("input");
            inputHidden.type = "hidden";
            inputHidden.value = midia.id;
            inputHidden.id = "idmidia";
            inputHidden.name = "idmidia";

            botoesMidia.appendChild(inputHidden);

            let buttonLista = document.createElement("button");
            buttonLista.onclick = function() {
                if (midia.naLista === 'sim') {
                    toggleListaRemover(this, midia.id);
                } else {
                    toggleLista(this, midia.id);
                }
            };
            buttonLista.className = midia.naLista === 'sim' ? "button-add-lista" : "button-add-lista";
            buttonLista.innerHTML = midia.naLista === 'sim' ? '<i class="fa-solid fa-check"></i>' : '<i class="fa-solid fa-plus"></i>';
            botoesMidia.appendChild(buttonLista);

            let buttonLike = document.createElement("button");
            buttonLike.className = "button-like";
            buttonLike.onclick = function() {
                if (midia.curtido === 'sim') {
                    descurtir(this, midia.id);
                } else {
                    curtir(this, midia.id);
                }
            };
            buttonLike.innerHTML = midia.curtido === 'sim' ? '<i class="fa-solid fa-thumbs-up"></i>' : '<i class="fa-regular fa-thumbs-up"></i>';
            botoesMidia.appendChild(buttonLike);

            detalhes.appendChild(botoesMidia);
            card.appendChild(detalhes);
            col.appendChild(card);
            row.appendChild(col);
        });

        container.appendChild(row);
        resultadoDiv.appendChild(container);
    }, 300);
}

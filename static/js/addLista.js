function toggleLista(button, midiaId) {
    const icone = button.querySelector("i");

    if (icone.classList.contains("fa-plus")) {
        // Adiciona a mídia à lista
        fetch('/adiciolista', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input_data: midiaId }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                icone.classList.remove("fa-plus");
                icone.classList.add("fa-check");
                button.setAttribute("onclick", `toggleListaRemover(this, '${midiaId}')`);
            }
        })
        .catch(error => console.error('Erro:', error));
    }
}

function toggleListaRemover(button, midiaId) {
    const icone = button.querySelector("i");

    // Remove a mídia da lista
    fetch('/removerlista', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input_data: midiaId }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            icone.classList.remove("fa-check");
            icone.classList.add("fa-plus");
            button.setAttribute("onclick", `toggleLista(this, '${midiaId}')`);
        }
    })
    .catch(error => console.error('Erro:', error));
}
function curtir(button, midiaId) {
    const icone = button.querySelector("i");

    if (icone.classList.contains("fa-regular")) {
        
        fetch('/curtir', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ input_data: midiaId }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                icone.classList.remove("fa-regular");
                icone.classList.add("fa-solid");
                button.setAttribute("onclick", `descurtir(this, '${midiaId}')`);
            }
        })
        .catch(error => console.error('Erro:', error));
    }
}

function descurtir(button, midiaId) {
    const icone = button.querySelector("i");

    // Remove a mídia da lista
    fetch('/descurtir', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input_data: midiaId }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            icone.classList.remove("fa-solid");
            icone.classList.add("fa-regular");
            button.setAttribute("onclick", `curtir(this, '${midiaId}')`);
        }
    })
    .catch(error => console.error('Erro:', error));
}

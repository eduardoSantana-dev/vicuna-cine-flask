const container = document.querySelector('.container-modal')
const modal = document.querySelector('.modal-add')
const nome = document.querySelector('.form-nome')
const fotos = document.querySelector('.select-foto')

function ativarModal(){
    container.classList.add('active')
    document.getElementById('acao').value = 'add';
}

function fecharModal(){
    modal.classList.add('fecharmodal');
 

  
    setTimeout(() => {
        modal.classList.remove('fecharmodal');
        container.classList.remove('active');
        modal.classList.remove('escolherfoto');
        nome.style.display = "flex";
        fotos.style.display = "none";
    }, 300);
}
function continuar(){
    modal.classList.add('escolherfoto')
    nome.style.display = "none"
    fotos.style.display= "flex"
}
container.addEventListener('click', (e) => {
    if (e.target === container) {
        modal.classList.add('fecharmodal');

        setTimeout(() => {
            modal.classList.remove('fecharmodal');
            container.classList.remove('active');
            modal.classList.remove('escolherfoto');
            nome.style.display = "flex";
            fotos.style.display = "none";
        }, 300); 
    }
});
function gerenciar(){
    const padrao = document.querySelectorAll('.padrao');
    const edit = document.querySelectorAll('.edit');

    padrao.forEach(element => {
        element.style.display = 'none';
    });

    edit.forEach(element => {
        element.style.display = 'block';
    });
}
function modaledit(nome,id){
    container.classList.add('active')
    document.getElementById('nomeinput').value = nome;
    document.getElementById('acao').value = 'edit';
    document.getElementById('idperfil').value = id;
    console.log(id)

}


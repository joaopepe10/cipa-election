function votar(candidato) {
    alert(`Você votou em: ${candidato}`);
 
}

function voltar() {
    alert('Voltando para a página anterior');
   

}
function abrirConfirmacao(nome, cargo) {

    const confirmacao = document.getElementById("confirmacao");
    confirmacao.style.display = "block";

    const candidatoSelecionado = document.getElementById("candidatoSelecionado");
    candidatoSelecionado.innerHTML = `${nome}<br>${cargo}`;
}

function confirmarVoto() {
    alert("Voto confirmado! Obrigado por votar.");
    fecharConfirmacao();
   
}

function fecharConfirmacao() {
    const confirmacao = document.getElementById("confirmacao");
    confirmacao.style.display = "none";
}

document.getElementById("novoUsuario").addEventListener("change", function() {
    const form = document.getElementById("loginForm");
    if (this.checked) {
        form.action = "/cadastro"; 
        form.querySelector(".button").textContent = "Cadastrar";
    } else {
        form.action = "/login";  
        form.querySelector(".button").textContent = "Entrar";
    }
});

function applyCandidate() {
    // IDs de exemplo. Substitua pelos valores reais de `IdEleicao` e `IdUsuario`.
    const IdEleicao = 1; // ID da eleição
    const IdUsuario = document.getElementById("usuario").value; // Pode ser o ID do usuário ou valor do campo "Usuário"

    // Construa a URL
    const url = `/api/elections/${IdEleicao}/apply-candidate/${IdUsuario}`;

    // Faça uma requisição para a URL
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
            // Inclua aqui os dados necessários na requisição
        })
    })
    .then(response => response.json())
    .then(data => {
        // Exibir o resultado ou realizar outra ação
        alert("Requisição realizada com sucesso: " + JSON.stringify(data));
    })
    .catch(error => {
        console.error("Erro na requisição:", error);
    });
}




// Tela inicial
function irParaHome() {
    window.location.href = '/';
}

// Script responsável pela tela de Votação

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

function confirmarCadastro(){
    alert("Usuário cadastrado com sucesso.");
    fecharConfirmacao();
}

function fecharConfirmacao() {
    const confirmacao = document.getElementById("confirmacao");
    confirmacao.style.display = "none";
}




//------------------------------------------------





//Script responsável pela Tela Cadastro Usuário
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

//------------------------------------------------






//Script responsável pela tela Cadastro Candidato
function irParaCandidato() {
    window.location.href = '/api/candidates/cadastro-candidato';
}

//função que redireciona para tela cadastro de usuario
function irParaCadastro() {
     window.location.href = `/api/users/cadastro-usuario`;
}

function submitUserForm() {
    const name = document.getElementById('name').value;
    const senha = document.getElementById('senha').value;
    const email = document.getElementById('email').value;

    const userData = {
        usuario: {
            name: name,
            email: email,
            senha: senha
        }
    };

    fetch('/api/users/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseMsg').innerText = data.msg || 'Usuário cadastrado com sucesso!';
        irParaHome();
    })
    .catch(error => console.error('Erro:', error));
}

/*


function submitForm() {
    const userId = document.getElementById('user_id').value;
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;


    fetch('/api/create_user/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: JSON.stringify({
            user_id: userId,
            name: name,
            email: email
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseMsg').innerText = data.msg || 'User created successfully!';
    })
    .catch(error => console.error('Error:', error));
}

*/




// Função para submissão do formulário de candidato
function submitCandidateForm() {
    const speech = document.getElementById('speech').value;
    const startDate = document.getElementById('start_date').value;
    const endDate = document.getElementById('end_date').value;

    const candidateData = {
        candidato: {
            speech: speech
        },
        eleicao: {
            start_date: startDate,
            end_date: endDate
        }
    };

    fetch('/api/candidates/create_candidate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(candidateData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('responseMsg').innerText = data.msg || 'CANDIDATO CADASTRADO COM SUCESSO!!';
        irParaHome();
    })
    .catch(error => console.error('Erro:', error));
}


//------------------------------------------------







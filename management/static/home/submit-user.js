import axios from "axios";

async function submitUserFormAxios() {
    const name = document.getElementById("name").value;
    const senha = document.getElementById("senha").value;
    const email = document.getElementById("email").value;

    const responseMsg = document.getElementById("responseMsg");

    try {
        const response = await axios.post('http://127.0.0.1:8000/api/users/', {
            name: name,
            senha: senha,
            email: email,
        });

        if (response.status === 201) {
            responseMsg.textContent = response.data.msg;
        }
    } catch (error) {
        if (error.response) {
            responseMsg.textContent = 'Erro: ' + JSON.stringify(error.response.data);
        } else {
            responseMsg.textContent = 'Erro ao conectar com o servidor.';
        }
    }
}

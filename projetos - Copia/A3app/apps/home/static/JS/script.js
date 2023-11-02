document.getElementById('add_client').addEventListener('submit', function (event) {
    event.preventDefault(); // Impedir o envio padrão do formulário

    const formData = new FormData(this);
    const endpointUrl = 'http://localhost:8000/clientes/clientes/';

    fetch(endpointUrl, {
        method: 'POST',
        body: formData,
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Cliente cadastrado com sucesso!');
                // Redirecione ou faça qualquer outra ação desejada
            } else {
                alert('Erro ao cadastrar o cliente. Verifique os dados e tente novamente.');
            }
        })
        .catch(error => {
            console.error('Erro na solicitação:', error);
        });
});

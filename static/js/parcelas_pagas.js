// selecione a checkbox1 e adicione um ouvinte de evento de clique
const checkbox1 = document.getElementById('id_mensalidade_paga');
checkbox1.addEventListener('click', function () {
    // se a checkbox1 estiver marcada, atualize a quantidade de parcelas_pagas
    if (checkbox1.checked) {
        const parcelasPagasElement = document.getElementById('id_parcelas_pagas');
        parcelasPagasElement.value = parseInt(parcelasPagasElement.value) + 1;
    }
});

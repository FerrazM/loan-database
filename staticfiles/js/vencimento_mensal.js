document.addEventListener("DOMContentLoaded", function () {
    // Obter referência aos campos de formulário "data" e "vencimento_mensal"
    const dataField = document.getElementById("id_data");
    const vencimentoMensalField = document.getElementById("id_vencimento_mensal");

    // Adicione um event listener para o campo "data"
    dataField.addEventListener("change", function () {
        // Obtenha a data do campo "data"
        const data = new Date(dataField.value);

        // Adicione um mês à data
        data.setMonth(data.getMonth() + 1);

        const formattedDate = `${("0" + data.getDate()).slice(-2)}/${("0" + (data.getMonth() + 1)).slice(-2)}/${data.getFullYear()}`;

        // Verifique se o campo "vencimento_mensal" está vazio
        if (!vencimentoMensalField.value) {
            // Atualize o valor do campo "vencimento_mensal" com a data atualizada
            vencimentoMensalField.value = formattedDate;
        }
    });
});
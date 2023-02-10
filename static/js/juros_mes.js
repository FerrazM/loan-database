window.addEventListener("load", function () {
    document.getElementById("id_valor").addEventListener("input", updatePayment);
    document.getElementById("id_juros").addEventListener("input", updatePayment);
});

function updatePayment() {
    let valor = parseFloat(document.getElementById("id_valor").value);
    let juros = document.getElementById("id_juros").value;


    if (valor && juros) {
        let jurosDecimal = parseFloat(juros.replace("%", "")) / 100;
        let juros_mes = valor * jurosDecimal;
        document.getElementById("id_juros_mes").value = juros_mes.toFixed(2);
    }
}
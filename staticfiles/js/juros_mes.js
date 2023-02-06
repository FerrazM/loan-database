document.getElementById("id_valor").addEventListener("input", updatePayment);
document.getElementById("id_juros").addEventListener("input", updatePayment);

function updatePayment() {
  let valor = document.getElementById("id_valor").value;
  let juros = document.getElementById("id_juros").value;
  
  if (valor && juros) {
    let jurosDecimal = parseFloat(juros.replace("%", "")) / 100;
    let pagamentoMensal = valor * jurosDecimal;
    document.getElementById("id_pagamento_mensal").value = pagamentoMensal.toFixed(2);
  }
}
$(document).ready(function() {
    const date = new Date(data);
    const ptBR = date.toLocaleDateString('pt-BR');
    $('#date-display').text(ptBR);
  });
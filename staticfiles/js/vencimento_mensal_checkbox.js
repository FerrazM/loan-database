$(document).ready(function () {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1;
    var yyyy = today.getFullYear();
    if (dd < 10) {
        dd = '0' + dd;
    }
    if (mm < 10) {
        mm = '0' + mm;
    }
    today = dd + '/' + mm + '/' + yyyy;

    var savedDay = $('input[name="vencimento_mensal"]').val().split('/')[0];

    $('input[name="vencimento_mensal"]').change(function () {
        if ($(this).val() === today) {
            $('input[name="checkbox1"]').prop('checked', false);
            var nextMonth = new Date();
            nextMonth.setMonth(nextMonth.getMonth() + 1);
            var nextMonthDD = savedDay; // mesmo dia do mês anterior
            var nextMonthMM = nextMonth.getMonth() + 1;
            var nextMonthYYYY = nextMonth.getFullYear();
            if (nextMonthMM < 10) {
                nextMonthMM = '0' + nextMonthMM;
            }
            var nextMonthDate = nextMonthDD + '/' + nextMonthMM + '/' + nextMonthYYYY;
            $('input[name="vencimento_mensal"]').val(nextMonthDate);
        } else {
            savedDay = $(this).val().split('/')[0];
        }
    });

    $('input[name="checkbox1"]').change(function () {
        if ($(this).is(':checked')) {
            var nextMonth = new Date();
            nextMonth.setMonth(nextMonth.getMonth() + 1);
            var nextMonthDD = savedDay; // mesmo dia do mês anterior
            var nextMonthMM = nextMonth.getMonth() + 1;
            var nextMonthYYYY = nextMonth.getFullYear();
            if (nextMonthMM < 10) {
                nextMonthMM = '0' + nextMonthMM;
            }
            var nextMonthDate = nextMonthDD + '/' + nextMonthMM + '/' + nextMonthYYYY;
            $('input[name="vencimento_mensal"]').val(nextMonthDate);
        }
    });
});





$(document).ready(function () {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1;
    var yyyy = today.getFullYear();
    if (dd < 10) {
        dd = '0' + dd
    }
    if (mm < 10) {
        mm = '0' + mm
    }
    today = yyyy + '-' + mm + '-' + dd;
    $('input[name="vencimento_mensal"]').change(function () {
        if ($(this).val() === today) {
            $('input[name="checkbox1"]').prop('checked', false);
            var nextMonth = new Date();
            nextMonth.setMonth(nextMonth.getMonth() + 1);
            var nextMonthDD = nextMonth.getDate();
            var nextMonthMM = nextMonth.getMonth() + 1;
            var nextMonthYYYY = nextMonth.getFullYear();
            if (nextMonthDD < 10) {
                nextMonthDD = '0' + nextMonthDD;
            }
            if (nextMonthMM < 10) {
                nextMonthMM = '0' + nextMonthMM;
            }
            var nextMonthDate = nextMonthYYYY + '-' + nextMonthMM + '-' + nextMonthDD;
            $('input[name="vencimento_mensal"]').val(nextMonthDate);
        }
    });
});
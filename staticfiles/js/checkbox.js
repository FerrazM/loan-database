function handleChange(checkbox1, clientId) {
    var paymentField = document.querySelector(`#payment-field-${clientId}`);
    if (checkbox1.checked) {
        paymentField.classList.remove("red-background");
        paymentField.classList.add("green-background");
    } else {
        paymentField.classList.remove("green-background");
        paymentField.classList.add("red-background");
    }
}
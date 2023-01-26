function handleChange(checkbox) {
    var paymentField = document.querySelector("paymentField")
    if (checkbox.checked) {
        paymentField.classList.remove("red-background");
        paymentField.classList.add("green-background");
    } else {
        paymentField.classList.remove("green-background");
        paymentField.classList.add("red-background");
    }
}

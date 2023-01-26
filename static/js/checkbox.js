document.getElementById("checkbox1").addEventListener("change", function () {
    if (this.checked) {
        document.getElementById("payment-field").classList.add("green-background");
        document.getElementById("payment-field").classList.remove("red-background");
    } else {
        document.getElementById("payment-field").classList.add("red-background");
        document.getElementById("payment-field").classList.remove("green-background");
    }
});

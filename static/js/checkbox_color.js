const checkbox = document.getElementById("checkbox1");
const jurosMes = document.getElementById("juros_mes");

checkbox.addEventListener("change", function () {
    if (this.checked) {
        jurosMes.classList.add("green");
    } else {
        jurosMes.classList.remove("green");
    }
});
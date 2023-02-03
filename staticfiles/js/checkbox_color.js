console.log(jurosMes);
const checkbox1 = document.querySelector("#checkbox1");
const jurosMes = document.querySelector("#juros_mes");

checkbox1.addEventListener("change", function () {
    if (checkbox1.checked) {
        jurosMes.classList.remove("red");
        jurosMes.classList.add("green");
    } else {
        jurosMes.classList.remove("green");
        jurosMes.classList.add("red");
    }
});
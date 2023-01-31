document.getElementById("searchInput").addEventListener("keyup", function () {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const table = document.getElementsByTagName("table")[0];
    const rows = table.getElementsByTagName("tr");

    for (let i = 0; i < rows.length; i++) {
        const name = rows[i].getElementsByTagName("td")[0].textContent.toLowerCase();
        if (name.indexOf(input) === -1) {
            rows[i].style.display = "none";
        } else {
            rows[i].style.display = "";
        }
    }
});
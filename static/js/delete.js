document.addEventListener("DOMContentLoaded", function () {
    let deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function () {
            let mahsulotId = this.getAttribute("data-id");
            let confirmDelete = document.getElementById("confirmDelete");
            confirmDelete.href = "/mahsulot-ochirish/" + mahsulotId; // O'chirish URL'si
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    let deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function () {
            let mijozId = this.getAttribute("data-id");
            let confirm_mijoz_Delete = document.getElementById("confirm_mijoz_Delete");
            confirm_mijoz_Delete.href = "/mijoz-ochirish/" + mijozId; // O'chirish URL'si
        });
    });
});

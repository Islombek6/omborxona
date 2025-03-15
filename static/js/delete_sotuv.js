document.addEventListener("DOMContentLoaded", function () {
    let deleteButtons = document.querySelectorAll(".delete-btn");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function () {
            let sotuvId = this.getAttribute("data-id");
            let confirm_sotuv_Delete = document.getElementById("confirm_sotuv_Delete");
            confirm_sotuv_Delete.href = "/sotuvlar/sotuv-ochirish/" + sotuvId;
        });
    });
});

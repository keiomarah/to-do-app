document.querySelectorAll(".flash-dismiss-btn").forEach((btn) => {
  btn.addEventListener("click", (e) => {
    const message = e.target.closest(".flashed-message");
    if (message) {
      message.classList.add("hide");
    }

    setTimeout(() => {
      message.remove();
    }, 300);
  });
});

const addTaskBtn = document.getElementById("add-task-btn");
const closeDialogBtn = document.getElementById("close-dialog-btn");
const addTaskDialog = document.getElementById("add-task-dialog");

addTaskBtn.addEventListener("click", () => {
  addTaskDialog.showModal();
});

closeDialogBtn.addEventListener("click", () => {
  addTaskDialog.close();
});

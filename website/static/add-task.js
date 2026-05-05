const addTaskBtn = document.getElementById("add-task-btn");
const addTaskBtn2 = document.getElementById("add-task-btn2");
const closeDialogBtn = document.getElementById("close-dialog-btn");
const addTaskDialog = document.getElementById("add-task-dialog");

if (addTaskBtn) {
  addTaskBtn.addEventListener("click", () => {
    addTaskDialog.showModal();
  });
}

if (addTaskBtn2) {
  addTaskBtn2.addEventListener("click", () => {
    addTaskDialog.showModal();
  });
}

if (closeDialogBtn) {
  closeDialogBtn.addEventListener("click", () => {
    addTaskDialog.close();
  });
}

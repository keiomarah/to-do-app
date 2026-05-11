const addTaskBtns = document.querySelectorAll(".add-task-btn");
const closeDialogBtn = document.getElementById("close-dialog-btn");
const addTaskDialog = document.getElementById("add-task-dialog");

addTaskBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    addTaskDialog.showModal();
  });
});

if (closeDialogBtn) {
  closeDialogBtn.addEventListener("click", () => {
    addTaskDialog.close();
  });
}

async function editTask(taskId) {
  const response = await fetch(`/task/${taskId}`);
  const task = await response.json();

  document.getElementById("task-id").value = task.id;
  document.getElementById("task_name").value = task.name;
  console.log(task.due);
  document.getElementById("due_date").value = task.due;

  addTaskDialog.showModal();
}

document.querySelectorAll(".dismiss-btn.flash-dismiss-btn").forEach((btn) => {
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
const tasks = document.querySelectorAll(".task");
const pendingTaskCounter = document.getElementById("pending-task-counter");
const highPriorityCounter = document.getElementById("high-priority-counter");
const totalTasksToday = document.getElementById("total-tasks-today");
const completedTasksToday = document.getElementById("completed-tasks-today");
const percentComplete = document.getElementById("percent-complete");
const progressBar = document.getElementById("progress-bar-solid");
let progressBarWidth = 0;
const today = new Date();
today.setHours(0, 0, 0, 0);
document.querySelectorAll("input[type='checkbox']").forEach((cb) => {
  cb.addEventListener("change", dailyProgressBar);
});

function pendingTasks() {
  let uncompleted = 0;

  const tasks = document.querySelectorAll(".task");
  tasks.forEach((task) => {
    const checkbox = task.querySelector('input[type="checkbox"]');
    if (!checkbox.checked) {
      uncompleted++;
    }
  });

  pendingTaskCounter.textContent = uncompleted;
}

function dailyProgressBar() {
  const tasks = document.querySelectorAll(".task");
  let totalToday = 0;
  let completeToday = 0;
  tasks.forEach((task) => {
    const dueDate = new Date(task.dataset.due);
    console.log(dueDate);
    dueDate.setHours(0, 0, 0, 0);
    const checkbox = task.querySelector("input[type='checkbox']");
    const complete = checkbox.checked;
    console.log(complete);
    if (dueDate.getTime() === today.getTime()) {
      totalToday++;
      if (complete) {
        completeToday++;
      }
    }
  });

  console.log(completeToday);
  totalTasksToday.textContent = totalToday;
  completedTasksToday.textContent = completeToday;
  let percent = 0;

  if (totalToday > 0) {
    percent = Math.round((completeToday / totalToday) * 100);
  }

  console.log(percent);
  percentComplete.textContent = percent;
  progressBarAnimation(percent);
}

function progressBarAnimation(percent) {
  let width = progressBarWidth;
  if (progressBarWidth < percent) {
    const id = setInterval(() => {
      if (width >= percent) {
        clearInterval(id);
        progressBarWidth = width;
      } else {
        width++;
        progressBar.style.width = width + "%";
      }
    }, 10);
  } else {
    const id = setInterval(() => {
      if (width <= percent) {
        clearInterval(id);
        progressBarWidth = percent;
      } else {
        width--;
        progressBar.style.width = width + "%";
      }
    }, 10);
  }
}
function highPriorityTasks() {
  let highPriority = 0;
  document.querySelectorAll(".task").forEach((task) => {
    priority = task.querySelector(".task-priority");
    if (priority.classList.contains("high")) {
      highPriority++;
    }

    highPriorityCounter.textContent = highPriority;
  });
}

function dailyProgressTasks() {}
addTaskBtn.addEventListener("click", () => {
  addTaskDialog.showModal();
});

closeDialogBtn.addEventListener("click", () => {
  addTaskDialog.close();
});

function updateTask(taskId) {
  fetch("/update-task", {
    method: "POST",
    body: JSON.stringify({ taskId: taskId }),
  })
    .then((res) => {
      window.location.href - "/";
      pendingTasks();
    })
    .then((res) => {
      dailyProgressBar();
    });
}

function deleteTask(taskId) {
  fetch("/delete-task", {
    method: "POST",
    body: JSON.stringify({ taskId: taskId }),
  })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById(`${taskId}-task`).remove();
      pendingTasks();
      highPriorityTasks();
      dailyProgressBar();
    });
}

pendingTasks();
highPriorityTasks();
dailyProgressBar();

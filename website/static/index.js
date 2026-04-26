document.querySelectorAll(".dismiss-btn").forEach((btn) => {
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

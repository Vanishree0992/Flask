document.addEventListener("DOMContentLoaded", () => {
  const timeLabel = document.getElementById("timeLabel");
  const timerBar = document.getElementById("timerBar");
  const quizForm = document.getElementById("quizForm");
  const timeoutMsg = document.getElementById("timeoutMsg");

  const TOTAL_TIME = 60; // match with app.py

  function updateTimer() {
    fetch('/api/timer')
      .then(res => res.json())
      .then(data => {
        const remaining = data.remaining;

        // Display remaining time
        timeLabel.textContent = `${remaining}s`;

        // Update progress bar
        const percent = (remaining / TOTAL_TIME) * 100;
        timerBar.style.width = percent + "%";

        if (remaining <= 0) {
          quizForm.querySelectorAll("input, button").forEach(el => el.disabled = true);
          timeoutMsg.classList.remove("d-none");
          clearInterval(timerInterval);
        }
      });
  }

  const timerInterval = setInterval(updateTimer, 1000);
  updateTimer(); // Initial call
});

document.addEventListener("DOMContentLoaded", () => {
  const buttons = document.querySelectorAll(".vote-btn");
  const messageBox = document.getElementById("messageBox");

  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      const candidate = btn.getAttribute("data-candidate");

      fetch("/api/vote", {
        method: "POST",
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ candidate })
      })
      .then(res => res.json())
      .then(data => {
        if (data.message) {
          showMessage(data.message, "success");
          updateResults(); // Refresh after voting
        } else if (data.error) {
          showMessage(data.error, "danger");
        }
      });
    });
  });

  function showMessage(msg, type) {
    messageBox.className = `alert alert-${type}`;
    messageBox.textContent = msg;
    messageBox.classList.remove("d-none");
    setTimeout(() => messageBox.classList.add("d-none"), 2500);
  }

  function updateResults() {
    fetch("/api/results")
      .then(res => res.json())
      .then(data => {
        data.results.forEach(candidate => {
          const bar = document.getElementById(`bar-${candidate.name}`);
          bar.style.width = `${candidate.percent.toFixed(1)}%`;
          bar.textContent = `${candidate.percent.toFixed(1)}% (${candidate.votes} votes)`;
        });
      });
  }

  // Initial load
  updateResults();

  // Poll every 5 seconds
  setInterval(updateResults, 5000);
});

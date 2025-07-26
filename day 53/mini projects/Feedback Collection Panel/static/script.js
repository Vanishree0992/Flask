document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("feedbackForm");
  const nameInput = document.getElementById("name");
  const messageInput = document.getElementById("message");
  const alertBox = document.getElementById("alertBox");
  const feedbackList = document.getElementById("feedbackList");

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const payload = {
      name: nameInput.value.trim(),
      message: messageInput.value.trim()
    };

    fetch("/api/feedback", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    .then(res => res.json())
    .then(data => {
      if (data.message) {
        alertBox.className = "alert alert-success mt-3";
        alertBox.textContent = data.message;
        alertBox.classList.remove("d-none");
        form.reset();
        loadFeedbacks();
      } else if (data.error) {
        alertBox.className = "alert alert-danger mt-3";
        alertBox.textContent = data.error;
        alertBox.classList.remove("d-none");
      }
    });
  });

  function loadFeedbacks() {
    fetch("/api/feedbacks")
      .then(res => res.json())
      .then(data => {
        feedbackList.innerHTML = '';
        if (data.length === 0) {
          feedbackList.innerHTML = "<li class='list-group-item'>No feedback yet.</li>";
        } else {
          data.forEach(fb => {
            const li = document.createElement("li");
            li.className = "list-group-item";
            li.innerHTML = `<strong>${fb.name}:</strong> ${fb.message}`;
            feedbackList.appendChild(li);
          });
        }
      });
  }

  loadFeedbacks();
});

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("taskForm");
  const taskInput = document.getElementById("taskInput");
  const taskTable = document.getElementById("taskTableBody");
  const alertBox = document.getElementById("alertBox");

  // POST new task via fetch
  form.addEventListener("submit", e => {
    e.preventDefault();
    const title = taskInput.value.trim();
    if (!title) return;

    fetch("/api/tasks", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title })
    })
    .then(res => res.json())
    .then(data => {
      const newTask = data.task;
      const row = document.createElement("tr");
      row.innerHTML = `<td>${newTask.id}</td><td>${newTask.title}</td>`;
      taskTable.appendChild(row);

      showAlert(`✅ Task "${newTask.title}" added!`);
      taskInput.value = "";
    });
  });

  function showAlert(message) {
    alertBox.textContent = message;
    alertBox.classList.remove("d-none");
    setTimeout(() => alertBox.classList.add("d-none"), 3000);
  }
});

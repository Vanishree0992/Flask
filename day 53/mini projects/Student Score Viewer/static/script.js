document.addEventListener("DOMContentLoaded", () => {
  const studentList = document.querySelectorAll(".student-item");
  const scoreContainer = document.getElementById("scoreContainer");

  studentList.forEach(item => {
    item.addEventListener("click", () => {
      const studentId = item.getAttribute("data-id");

      // Clear existing scores
      scoreContainer.innerHTML = `<div class="text-muted">Loading scores...</div>`;

      fetch(`/api/score/${studentId}`)
        .then(res => res.json())
        .then(data => {
          if (data.error) {
            scoreContainer.innerHTML = `<div class="alert alert-danger">${data.error}</div>`;
          } else {
            let html = '';
            for (let subject in data) {
              html += `
                <div class="col">
                  <div class="card shadow-sm">
                    <div class="card-body">
                      <h5 class="card-title">${subject}</h5>
                      <p class="card-text">Score: <strong>${data[subject]}</strong></p>
                    </div>
                  </div>
                </div>
              `;
            }
            scoreContainer.innerHTML = html;
          }
        })
        .catch(() => {
          scoreContainer.innerHTML = `<div class="alert alert-danger">Failed to fetch scores.</div>`;
        });
    });
  });
});

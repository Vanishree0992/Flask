document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("editForm");
  const userId = document.getElementById("userId").value;
  const nameInput = document.getElementById("nameInput");
  const emailInput = document.getElementById("emailInput");

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    fetch(`/api/user/${userId}`, {
      method: "PUT",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: nameInput.value.trim(),
        email: emailInput.value.trim()
      })
    })
    .then(res => res.json())
    .then(data => {
      if (data.success) {
        window.location.reload();
      } else {
        alert(data.error || "Update failed.");
      }
    });
  });
});

document.addEventListener("DOMContentLoaded", () => {
  const badge = document.getElementById("userCountBadge");
  const alertBox = document.getElementById("flashAlert");
  let previousCount = 0;

  function fetchCount() {
    fetch("/api/users/count")
      .then(res => res.json())
      .then(data => {
        const newCount = data.count;
        badge.textContent = newCount;

        if (newCount > previousCount && previousCount !== 0) {
          showFlashAlert();
        }

        previousCount = newCount;
      });
  }

  function showFlashAlert() {
    alertBox.classList.remove("d-none");
    setTimeout(() => {
      alertBox.classList.add("d-none");
    }, 2000);
  }

  // Initial fetch
  fetchCount();

  // Poll every 5 seconds
  setInterval(fetchCount, 5000);
});

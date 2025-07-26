document.addEventListener("DOMContentLoaded", () => {
  const alertContainer = document.getElementById("alertContainer");

  function fetchAlerts() {
    fetch("/api/weather/alerts")
      .then(res => res.json())
      .then(data => {
        if (data.length === 0) {
          alertContainer.innerHTML = '<div class="alert alert-secondary text-center">No weather alerts at this time.</div>';
          return;
        }

        alertContainer.innerHTML = data.map(alert => `
          <div class="alert alert-${alert.type}" role="alert">
            ${alert.message}
          </div>
        `).join('');
      })
      .catch(() => {
        alertContainer.innerHTML = '<div class="alert alert-danger text-center">Failed to load weather alerts.</div>';
      });
  }

  fetchAlerts(); // Initial call
  setInterval(fetchAlerts, 15000); // Refresh every 15 seconds
});

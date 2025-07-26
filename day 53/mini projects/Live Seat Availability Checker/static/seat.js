document.addEventListener("DOMContentLoaded", () => {
  const seatGrid = document.getElementById("seatGrid");
  const lastUpdated = document.getElementById("lastUpdated");

  function fetchSeats() {
    fetch("/api/seats")
      .then(res => res.json())
      .then(data => {
        seatGrid.innerHTML = "";

        for (const [seat, isAvailable] of Object.entries(data)) {
          const btn = document.createElement("button");
          btn.className = `btn seat-btn ${isAvailable ? 'btn-success' : 'btn-danger'}`;
          btn.textContent = seat;
          btn.disabled = !isAvailable;
          seatGrid.appendChild(btn);
        }

        const now = new Date();
        lastUpdated.textContent = `Last updated: ${now.toLocaleTimeString()}`;
      })
      .catch(() => {
        seatGrid.innerHTML = '<div class="alert alert-danger">Error loading seat data.</div>';
      });
  }

  fetchSeats();                    // Initial fetch
  setInterval(fetchSeats, 15000);  // Refresh every 15 seconds
});

document.addEventListener("DOMContentLoaded", () => {
  const clockDisplay = document.getElementById("clockDisplay");

  function updateClock() {
    fetch('/api/time')
      .then(res => res.json())
      .then(data => {
        const { hour, minute, second } = data;
        const formattedTime = `${String(hour).padStart(2, '0')} : ${String(minute).padStart(2, '0')} : ${String(second).padStart(2, '0')}`;
        clockDisplay.textContent = formattedTime;
      })
      .catch(() => {
        clockDisplay.textContent = "Error fetching time.";
      });
  }

  setInterval(updateClock, 1000);
});

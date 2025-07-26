document.addEventListener("DOMContentLoaded", () => {
  const timeDisplay = document.getElementById("timeDisplay");

  function updateTime() {
    fetch("/api/time")
      .then(res => res.json())
      .then(data => {
        timeDisplay.style.opacity = 0.3;
        setTimeout(() => {
          timeDisplay.textContent = data.time;
          timeDisplay.style.opacity = 1;
        }, 200);
      });
  }

  updateTime(); // initial call
  setInterval(updateTime, 1000); // update every second
});

function updateWeather() {
  const spinner = document.getElementById("spinner");
  spinner.style.display = "inline-block";

  fetch('/api/weather')
    .then(res => res.json())
    .then(data => {
      document.getElementById("temp").textContent = `Temperature: ${data.temperature} °C`;
      document.getElementById("humidity").textContent = `Humidity: ${data.humidity} %`;
      document.getElementById("status").textContent = `Status: ${data.status}`;
      document.getElementById("lastUpdated").textContent = `Last updated: ${new Date().toLocaleTimeString()}`;
    })
    .catch(() => {
      document.getElementById("temp").textContent = "Temperature: Error";
      document.getElementById("humidity").textContent = "Humidity: Error";
      document.getElementById("status").textContent = "Status: Error";
    })
    .finally(() => {
      spinner.style.display = "none";
    });
}

// Initial fetch
updateWeather();

// Poll every 10 seconds
setInterval(updateWeather, 10000);

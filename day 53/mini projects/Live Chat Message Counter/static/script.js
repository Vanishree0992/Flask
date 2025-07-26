document.addEventListener("DOMContentLoaded", () => {
  const messageCount = document.getElementById("messageCount");

  async function updateCount() {
    try {
      const res = await fetch("/api/messages/count");
      const data = await res.json();
      messageCount.textContent = data.count;
    } catch {
      messageCount.textContent = "⚠️";
    }
  }

  updateCount(); // initial load
  setInterval(updateCount, 5000); // poll every 5 seconds
});

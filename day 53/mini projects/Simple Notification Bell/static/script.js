document.addEventListener("DOMContentLoaded", () => {
  const notifCount = document.getElementById("notifCount");
  const notificationList = document.getElementById("notificationList");

  async function fetchNotifications(showList = false) {
    try {
      const res = await fetch("/api/notifications");
      const data = await res.json();

      notifCount.textContent = data.unread_count;

      if (showList) {
        if (data.unread_count === 0) {
          notificationList.innerHTML = `<div class="text-muted">No new notifications.</div>`;
        } else {
          notificationList.innerHTML = data.messages.map(msg => `
            <div class="alert alert-info mb-2">${msg.message}</div>
          `).join('');
        }
      }
    } catch (err) {
      notifCount.textContent = "!";
      if (showList) {
        notificationList.innerHTML = `<div class="alert alert-danger">Error loading notifications.</div>`;
      }
    }
  }

  // Fetch count every 10 seconds
  setInterval(() => fetchNotifications(false), 10000);
  fetchNotifications(false); // initial fetch

  // When modal is opened, fetch full list
  document.getElementById("bellIcon").addEventListener("click", () => {
    fetchNotifications(true);
  });
});

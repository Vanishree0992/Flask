document.addEventListener("DOMContentLoaded", () => {
  // 1. Fetch updates and update rows
  fetch(userApiUrl)
    .then(res => res.json())
    .then(data => {
      data.forEach(u => {
        const row = document.querySelector(`tr[data-userid="${u.id}"]`);
        if (row) {
          row.children[1].textContent = u.name;
          row.children[2].innerHTML = `<span class="badge ${u.status === 'active' ? 'bg-success' : 'bg-secondary'}">${u.status}</span>`;
        }
      });
    });

  // 4. url_for used in userApiUrl

  // 5. Button click from Jinja2 loop
  document.querySelectorAll(".product-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      const product = btn.dataset.product;
      document.getElementById("productSection").innerHTML = `<b>Product:</b> ${product} (loaded via JS)`;
    });
  });

  // 6. Render and update chart
  const ctx = document.getElementById('userChart').getContext('2d');
  const userChart = new Chart(ctx, {
    type: 'bar',
    data: { labels: [], datasets: [{ label: 'Monthly Data', data: [] }] }
  });

  fetch('/api/chart-data')
    .then(res => res.json())
    .then(data => {
      userChart.data.labels = data.labels;
      userChart.data.datasets[0].data = data.values;
      userChart.update();
    });

  // 8. Dropdown filter
  document.getElementById("filterDropdown").addEventListener("change", e => {
    const selected = e.target.value.toLowerCase();
    document.querySelectorAll("#userTable tbody tr").forEach(row => {
      const name = row.children[1].textContent.toLowerCase();
      row.style.display = selected === "all" || name === selected ? "" : "none";
    });
  });

  // 10. Sorting table (basic)
  document.querySelector("#userTable thead").addEventListener("click", () => {
    const rows = Array.from(document.querySelectorAll("#userTable tbody tr"));
    rows.sort((a, b) => a.children[1].textContent.localeCompare(b.children[1].textContent));
    const tbody = document.querySelector("#userTable tbody");
    rows.forEach(r => tbody.appendChild(r));
  });
});

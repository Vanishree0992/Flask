document.addEventListener("DOMContentLoaded", () => {
  // 1. Time button
  document.getElementById("loadTimeBtn").onclick = () => {
    fetch("/api/time")
      .then(res => res.json())
      .then(data => {
        document.getElementById("timeDisplay").innerText = `Time: ${data.time}`;
      });
  };

  // 3. Load users on page load
  fetch("/api/users")
    .then(res => res.json())
    .then(users => {
      const tbody = document.getElementById("userTableBody");
      users.forEach(u => {
        tbody.innerHTML += `<tr><td>${u.id}</td><td>${u.name}</td></tr>`;
      });
    });

  // 4. Load more products
  document.getElementById("loadMoreBtn").onclick = () => {
    fetch("/api/products")
      .then(res => res.json())
      .then(products => {
        const list = document.getElementById("productList");
        products.forEach(p => {
          list.innerHTML += `<li>${p.name} - ₹${p.price}</li>`;
        });
      });
  };

  // 5. Submit form via fetch
  document.getElementById("sampleForm").onsubmit = e => {
    e.preventDefault();
    const inputVal = e.target.input.value;
    document.getElementById("spinner").style.display = 'inline-block';

    fetch("/api/submit", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ input: inputVal })
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById("formResponse").innerText = data.message;
      document.getElementById("spinner").style.display = 'none';
    });
  };

  // 9. PUT request
  document.getElementById("sendPutBtn").onclick = () => {
    fetch("/api/put-example", {
      method: "PUT",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ update: "new value" })
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById("putResponse").innerText = JSON.stringify(data);
    });
  };

  // 7. Fetch joke
  document.getElementById("jokeBtn").onclick = () => {
    fetch("/api/random")
      .then(res => res.json())
      .then(data => {
        const alert = document.getElementById("jokeAlert");
        alert.style.display = 'block';
        alert.innerText = data.joke;
      });
  };

  // 11. Live search
  document.getElementById("searchInput").oninput = e => {
    const q = e.target.value;
    fetch(`/api/search?q=${q}`)
      .then(res => res.json())
      .then(results => {
        const ul = document.getElementById("searchResults");
        ul.innerHTML = "";
        results.forEach(name => {
          ul.innerHTML += `<li>${name}</li>`;
        });
      });
  };

  // 12. Polling time every 5 sec
  setInterval(() => {
    fetch("/api/time")
      .then(res => res.json())
      .then(data => {
        document.getElementById("liveTime").innerText = data.time;
      });
  }, 5000);

  // 14. Async/await example
  document.getElementById("statusBtn").onclick = async () => {
    const res = await fetch("/api/status");
    const data = await res.json();
    document.getElementById("statusResult").innerText = `Status: ${data.status}, Uptime: ${data.uptime}`;
  };
});

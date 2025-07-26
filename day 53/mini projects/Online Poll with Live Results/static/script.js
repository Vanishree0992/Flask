document.addEventListener("DOMContentLoaded", () => {
  let chart;
  const pollQuestion = document.getElementById("pollQuestion");
  const optionsContainer = document.getElementById("optionsContainer");

  function loadPoll() {
    fetch("/api/poll")
      .then(res => res.json())
      .then(data => {
        pollQuestion.textContent = data.question;

        optionsContainer.innerHTML = '';
        data.options.forEach((option, index) => {
          const btn = document.createElement("button");
          btn.textContent = option;
          btn.className = "btn btn-outline-primary m-2";
          btn.onclick = () => submitVote(index);
          optionsContainer.appendChild(btn);
        });

        renderChart(data.options, data.votes);
      });
  }

  function submitVote(optionIndex) {
    fetch("/api/vote", {
      method: "POST",
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ option: optionIndex })
    })
    .then(res => {
      if (res.ok) {
        return res.json();
      } else {
        location.reload();  // trigger flash on double vote
        throw new Error("Already voted");
      }
    })
    .then(() => {
      loadPoll();
    });
  }

  function renderChart(labels, data) {
    if (chart) {
      chart.data.datasets[0].data = data;
      chart.update();
    } else {
      const ctx = document.getElementById('resultChart').getContext('2d');
      chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels,
          datasets: [{
            label: 'Votes',
            data,
            backgroundColor: ['#4e79a7', '#f28e2c', '#e15759', '#76b7b2']
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: false }
          },
          scales: {
            y: { beginAtZero: true }
          }
        }
      });
    }
  }

  // Initial load + poll every 5s
  loadPoll();
  setInterval(loadPoll, 5000);
});

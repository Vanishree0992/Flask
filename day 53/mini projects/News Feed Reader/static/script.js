document.addEventListener("DOMContentLoaded", () => {
  const newsArea = document.getElementById("newsArea");

  function fetchNews() {
    newsArea.innerHTML = `<div class="text-center text-muted">⏳ Loading news...</div>`;

    fetch("/api/news")
      .then(res => res.json())
      .then(data => {
        if (!data.articles || data.articles.length === 0) {
          newsArea.innerHTML = `<div class="alert alert-warning">No news available.</div>`;
          return;
        }

        let html = `
          <h5 class="mb-3">Category: <span class="badge bg-primary">${data.category}</span></h5>
          <div class="accordion" id="newsAccordion">
        `;

        data.articles.forEach((article, index) => {
          html += `
            <div class="accordion-item">
              <h2 class="accordion-header" id="heading${index}">
                <button class="accordion-button ${index !== 0 ? 'collapsed' : ''}" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${index}">
                  ${article.title}
                </button>
              </h2>
              <div id="collapse${index}" class="accordion-collapse collapse ${index === 0 ? 'show' : ''}" data-bs-parent="#newsAccordion">
                <div class="accordion-body">
                  ${article.content}
                </div>
              </div>
            </div>
          `;
        });

        html += "</div>";
        newsArea.innerHTML = html;
      })
      .catch(() => {
        newsArea.innerHTML = `<div class="alert alert-danger">Failed to load news.</div>`;
      });
  }

  fetchNews(); // initial call
});

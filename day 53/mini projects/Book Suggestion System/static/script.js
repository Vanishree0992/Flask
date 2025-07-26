document.addEventListener("DOMContentLoaded", () => {
  const suggestBtn = document.getElementById("suggestBtn");
  const bookTitle = document.getElementById("bookTitle");
  const bookAuthor = document.getElementById("bookAuthor");
  const bookSummary = document.getElementById("bookSummary");

  const modal = new bootstrap.Modal(document.getElementById("bookModal"));

  suggestBtn.addEventListener("click", () => {
    fetch("/api/book/suggest")
      .then(res => res.json())
      .then(data => {
        bookTitle.textContent = data.title;
        bookAuthor.textContent = data.author;
        bookSummary.textContent = data.summary;
        modal.show();
      });
  });
});

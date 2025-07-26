document.addEventListener("DOMContentLoaded", () => {
  const quoteText = document.getElementById("quoteText");
  const quoteAuthor = document.getElementById("quoteAuthor");
  const spinner = document.getElementById("spinner");
  const newQuoteBtn = document.getElementById("newQuoteBtn");

  newQuoteBtn.addEventListener("click", () => {
    spinner.style.display = "inline-block";
    quoteText.style.opacity = "0.3";
    quoteAuthor.style.opacity = "0.3";

    fetch("/api/quote")
      .then(res => res.json())
      .then(data => {
        quoteText.textContent = data.text;
        quoteAuthor.textContent = "— " + data.author;
      })
      .catch(() => {
        quoteText.textContent = "Failed to load quote.";
        quoteAuthor.textContent = "";
      })
      .finally(() => {
        spinner.style.display = "none";
        quoteText.style.opacity = "1";
        quoteAuthor.style.opacity = "1";
      });
  });
});

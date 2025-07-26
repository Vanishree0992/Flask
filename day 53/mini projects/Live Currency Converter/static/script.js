document.addEventListener("DOMContentLoaded", () => {
  const amountInput = document.getElementById("amountInput");
  const currencySelect = document.getElementById("currencySelect");
  const resultBox = document.getElementById("resultBox");

  function fetchConversion() {
    const amount = amountInput.value;
    const toCurrency = currencySelect.value;

    fetch(`/api/convert?amount=${amount}&to=${toCurrency}`)
      .then(res => res.json())
      .then(data => {
        if (data.converted !== undefined) {
          resultBox.className = "alert alert-success";
          resultBox.textContent = `💱 ${amount} in ${toCurrency} = ${data.converted}`;
        } else {
          resultBox.className = "alert alert-danger";
          resultBox.textContent = data.error || "Conversion error.";
        }
      })
      .catch(() => {
        resultBox.className = "alert alert-danger";
        resultBox.textContent = "Something went wrong.";
      });
  }

  // Trigger conversion on input or currency change
  amountInput.addEventListener("input", fetchConversion);
  currencySelect.addEventListener("change", fetchConversion);

  fetchConversion(); // Initial load
});

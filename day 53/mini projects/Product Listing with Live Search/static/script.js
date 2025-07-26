document.addEventListener("DOMContentLoaded", () => {
  const searchInput = document.getElementById("searchInput");
  const productContainer = document.getElementById("productContainer");
  const loadingText = document.getElementById("loading");

  function renderProducts(products) {
    productContainer.innerHTML = "";

    if (products.length === 0) {
      productContainer.innerHTML = "<p>No products found.</p>";
      return;
    }

    products.forEach(product => {
      const col = document.createElement("div");
      col.className = "col-md-4 mb-4";

      const card = document.createElement("div");
      card.className = "card h-100 shadow";

      const cardBody = document.createElement("div");
      cardBody.className = "card-body";

      const title = document.createElement("h5");
      title.className = "card-title";
      title.textContent = product.name;

      const price = document.createElement("p");
      price.className = "card-text text-success";
      price.textContent = product.price;

      cardBody.appendChild(title);
      cardBody.appendChild(price);
      card.appendChild(cardBody);
      col.appendChild(card);
      productContainer.appendChild(col);
    });
  }

  function fetchProducts(query = "") {
    loadingText.style.display = "block";
    fetch(`/api/products?q=${encodeURIComponent(query)}`)
      .then(res => res.json())
      .then(data => {
        renderProducts(data);
      })
      .finally(() => {
        loadingText.style.display = "none";
      });
  }

  searchInput.addEventListener("input", () => {
    const query = searchInput.value.trim();
    fetchProducts(query);
  });

  // Load all products on initial page load
  fetchProducts();
});

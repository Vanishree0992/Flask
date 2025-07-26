document.addEventListener("DOMContentLoaded", () => {
  const progressBar = document.getElementById("progressBar");
  const productGrid = document.getElementById("productGrid");

  document.getElementById("loadBtn").onclick = () => {
    progressBar.style.width = '30%';
    progressBar.innerText = 'Loading...';

    fetch('/api/products')
      .then(res => res.json())
      .then(data => {
        progressBar.style.width = '100%';
        progressBar.innerText = 'Complete';

        productGrid.innerHTML = "";
        data.forEach(p => {
          productGrid.innerHTML += `
            <div class="col-md-4">
              <div class="card mb-3">
                <div class="card-body">
                  <h5>${p.name}</h5>
                  <p>Price: ₹${p.price}</p>
                </div>
              </div>
            </div>`;
        });

        new bootstrap.Toast(document.getElementById("successToast")).show();
      })
      .catch(() => {
        document.getElementById("errorAlert").classList.remove("d-none");
      });
  };
});

function loadPage(page) {
  fetch(`/api/items?page=${page}`)
    .then(res => res.json())
    .then(items => {
      const modal = new bootstrap.Modal(document.getElementById("myModal"));
      document.getElementById("modalBody").innerText = JSON.stringify(items, null, 2);
      modal.show();
    });
}

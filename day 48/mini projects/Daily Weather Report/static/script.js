document.addEventListener("DOMContentLoaded", function () {
    if (typeof temperatureData !== 'undefined') {
        const ctx = document.getElementById('tempChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['6AM', '9AM', '12PM', '3PM', '6PM', '9PM', '12AM'],
                datasets: [{
                    label: 'Hourly Temp (°C)',
                    data: temperatureData,
                    fill: true,
                    backgroundColor: 'rgba(255, 206, 86, 0.2)',
                    borderColor: '#f39c12',
                    tension: 0.3
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: false
                    }
                }
            }
        });
    }
});

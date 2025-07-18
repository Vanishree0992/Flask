document.addEventListener("DOMContentLoaded", function () {
    if (typeof eventDate === "undefined") return;

    const countdownElem = document.getElementById("countdown");

    function updateCountdown() {
        const now = new Date().getTime();
        const distance = eventDate.getTime() - now;

        if (distance <= 0) {
            countdownElem.innerText = "🎉 Event Started!";
            clearInterval(timer);
            return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        countdownElem.innerText = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }

    const timer = setInterval(updateCountdown, 1000);
    updateCountdown();
});

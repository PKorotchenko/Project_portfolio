document.addEventListener('DOMContentLoaded', function () {
    const cards = document.querySelectorAll('.project-card');
    cards.forEach(function (card) {
        card.addEventListener('click', function (event) {
            const link = event.target.closest('a');
            if (link) {
                return;
            }
            card.classList.toggle('glass-clicked');
        });
    });
});

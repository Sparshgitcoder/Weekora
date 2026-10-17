// main.js — students will add JavaScript here as features are built

// Landing page: filter trip cards by category
var filterButtons = document.querySelectorAll("[data-filter]");
var tripCards = document.querySelectorAll(".trip-card[data-category]");
var tripCount = document.querySelector("[data-trip-count]");
var tripsEmpty = document.querySelector("[data-trips-empty]");

filterButtons.forEach(function (button) {
    button.addEventListener("click", function () {
        var filter = button.dataset.filter;
        var shown = 0;

        filterButtons.forEach(function (other) {
            var active = other === button;
            other.classList.toggle("is-active", active);
            other.setAttribute("aria-pressed", active);
        });

        tripCards.forEach(function (card) {
            var match = filter === "all" || card.dataset.category === filter;
            card.hidden = !match;
            if (match) shown++;
        });

        if (tripCount) tripCount.textContent = shown + (shown === 1 ? " trip" : " trips");
        if (tripsEmpty) tripsEmpty.hidden = shown > 0;
    });
});

// Landing page: hide the floating scroll arrow once the trips are reached
var scrollCue = document.querySelector("[data-scroll-cue]");
var tripsSection = document.getElementById("trips");

if (scrollCue && tripsSection && "IntersectionObserver" in window) {
    new IntersectionObserver(function (entries) {
        var entry = entries[0];
        var reached = entry.isIntersecting || entry.boundingClientRect.top < 0;
        scrollCue.classList.toggle("is-hidden", reached);
    }).observe(tripsSection);
}

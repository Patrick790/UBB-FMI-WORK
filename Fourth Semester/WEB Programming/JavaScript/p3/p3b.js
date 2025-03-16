const matrix = [
    "ananas.png", "ananas.png",
    "capsuna.jpg", "capsuna.jpg",
    "kiwi.jpg", "kiwi.jpg",
    "mar.jpg", "mar.jpg"
];

matrix.sort(function () {
    return 0.5 - Math.random();
});

let first = null;
let second = null;

let matchedPairs = 0;

function checkPair() {
    let id1 = first.id;
    let id2 = second.id;

    if (matrix[id1] === matrix[id2]) {
        first.removeEventListener("click", selectie);
        second.removeEventListener("click", selectie);
        first.style.backgroundColor = "orange";
        second.style.backgroundColor = "orange";

        first = null;
        second = null;

        matchedPairs++;

        if (matchedPairs === matrix.length / 2) {
            alert("You won");
        }
    } else {
        setTimeout(function () {
            first.style.backgroundImage = "none"; // Remove the background image
            second.style.backgroundImage = "none"; // Remove the background image

            first = null;
            second = null;
        }, 1000);
    }
}

function selectie() {
    if (first && second) {
        return;
    }

    if (this === first) {
        return;
    }

    this.style.backgroundImage = `url(${matrix[this.id]})`; // Set background image

    if (!first) {
        first = this;
        return;
    }

    second = this;
    checkPair();
}

const elements = document.getElementsByTagName("td");
for (let i = 0; i < elements.length; i++) {
    elements[i].addEventListener("click", selectie);
}

$(document).ready(function(){
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
        let id1 = $(first).attr('id');
        let id2 = $(second).attr('id');

        if (matrix[id1] === matrix[id2]) {
            $(first).off("click", selectie);
            $(second).off("click", selectie);
            $(first).css("background-color", "orange");
            $(second).css("background-color", "orange");

            first = null;
            second = null;

            matchedPairs++;

            if (matchedPairs === matrix.length / 2) {
                alert("You won");
            }
        } else {
            setTimeout(function () {
                $(first).css("background-image", "none");
                $(second).css("background-image", "none");

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

        $(this).css("background-image", `url(${matrix[$(this).attr('id')]})`);

        if (!first) {
            first = this;
            return;
        }

        second = this;
        checkPair();
    }

    $("td").on("click", selectie);
});

$(document).ready(function (id){
    const imageList = $('#image-list');
    const listItems = imageList.find('li');
    listItems.eq(0).hide();
    let currentIndex = 0;
    let intervalId = null;

    function showNext() {
        clearInterval(intervalId)
        listItems.eq(currentIndex - 1).hide();
        currentIndex = (currentIndex + 1) % listItems.length;
        listItems.eq(currentIndex - 1).show();
        startInterval();
    }

    function showPrevious() {
        clearInterval(intervalId);
        listItems.eq(currentIndex - 1).hide();
        currentIndex = (currentIndex - 1 + listItems.length) % listItems.length;
        listItems.eq(currentIndex - 1).show();
        startInterval();
    }

    function startInterval() {
        intervalId = setInterval(showNext, 3000);
    }


    const nextButton = $('#next-button');
    nextButton.on('click', showNext);
    const previousButton = $('#previous-button');
    previousButton.on('click', showPrevious);

    startInterval();
});

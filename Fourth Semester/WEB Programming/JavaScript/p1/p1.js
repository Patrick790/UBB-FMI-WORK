const list1 = document.getElementById("cars");
const list2 = document.getElementById("flowers");

list1.addEventListener("dblclick", function () {
    const element = list1.options[list1.selectedIndex];
    list2.appendChild(element);
    list1.removeChild(element);
});

list2.addEventListener("dblclick", function () {
    const element = list2.options[list2.selectedIndex];
    list1.appendChild(element);
    list2.removeChild(element);
});

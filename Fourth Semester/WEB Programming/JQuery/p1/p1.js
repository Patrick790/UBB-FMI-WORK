$(document).ready(function(){
    $("#cars, #flowers").on("dblclick", function () {
        var selectedOption = $(this).find("option:selected");
        if ($(this).attr("id") === "cars") {
            selectedOption.appendTo("#flowers");
        } else {
            selectedOption.appendTo("#cars");
        }
    });
});



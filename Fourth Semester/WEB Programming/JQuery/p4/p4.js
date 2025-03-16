function sortColumn(tableId, columnIndex) {
    var table = $("#" + tableId);
    var rows, switching, i, x, y, shouldSwitch;
    switching = true;
    while (switching) {
        switching = false;
        rows = table.find("tr");
        for (i = 1; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = $(rows[i]).find("td").eq(columnIndex);
            y = $(rows[i + 1]).find("td").eq(columnIndex);
            if (parseFloat(x.text()) > parseFloat(y.text()) || (columnIndex === 0 && x.text().toLowerCase() > y.text().toLowerCase())) {
                shouldSwitch = true;
                break;
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }
}

function sortRow(rowIndex) {
    var table = $("#table2");
    var rows = table.find("tr");
    var columns = [];
    for (index = 0; index < rows.eq(0).children().length - 1; index++) {
        columns.push([]);
    }
    for (index = 0; index < rows.length; index++) {
        for (nthChild = 1; nthChild < rows[index].children.length; nthChild++) {
            columns[nthChild - 1].push($(rows[index]).children().eq(nthChild).find("div").text());
        }
    }

    function ascending(a, b) {
        if (a[rowIndex] < b[rowIndex]) {
            return -1;
        }
        if (a[rowIndex] > b[rowIndex]) {
            return 1;
        }
        return 0;
    }

    function descending(a, b) {
        if (a[rowIndex] > b[rowIndex]) {
            return -1;
        }
        if (a[rowIndex] < b[rowIndex]) {
            return 1;
        }
        return 0;
    }

    var before = columns.toString();
    if (!isNaN(parseInt(columns[0][rowIndex]))) {
        for (index = 0; index < columns.length; index++) {
            columns[index][rowIndex] = parseInt(columns[index][rowIndex]);
        }
    }
    columns.sort(ascending);
    if (before === columns.toString()) {
        columns.sort(descending);
    }

    for (var index = 0; index < rows.length; index++) {
        for (var nthChild = 0; nthChild < rows[index].children.length - 1; nthChild++) {
            $(rows[index]).children().eq(nthChild + 1).find("div").text(columns[nthChild][index]);
        }
    }
}

// Забираем таблицу из HTML-файла.

const table = document.querySelector('table');
let colIndex = -1;

const sortTable = function(index, type, isSorted) {
    const tbody = table.querySelector('tbody');

    const comp = function(row1, row2) {
        const rowData1 = row1.cells[index].innerHTML;
        const rowData2 = row2.cells[index].innerHTML;

        switch(type) {
            case 'integer':
                return rowData1 - rowData2;
                break;
            case 'text':
                if (rowData1 < rowData2) return -1;
                if (rowData1 > rowData2) return 1;
                return 0;
            case 'double':
                return rowData1 - rowData2;

        }
    }

    let rows = [].slice.call(tbody.rows);

    rows.sort(comp);
    if (isSorted) rows.reverse();

    table.removeChild(tbody);

    for(let i = 0; i < rows.length; i++) {
        tbody.appendChild(rows[i]);
    }

    table.appendChild(tbody);
};


table.addEventListener('click', (e) => {
    const el = e.target;
    if (el.nodeName != 'TH') return;
    
    const index = el.cellIndex;
    const type = el.getAttribute('data-type');
    sortTable(index, type, colIndex == index);
    if (colIndex == index) {
        colIndex = -1;
    }
    else {
        colIndex = index;
    }
});
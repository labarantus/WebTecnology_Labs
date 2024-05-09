var h1_hide = 1;

$(document).ready(function() {
    
    $(".hidebox p").hide();
    $(".hidebox h1").css("background-color", "#1e1e1e");
    $(".hidebox h1").css("color", "#ffffff");
    $(".page-header span").html()

    $(".product-pic img").hover(function() {

        $(this).animate({

            height: "308",
            width: "242",

        }, "fast");
    }, function() {

        $(this).animate({

            height: "280",
            width: "220",

        }, "fast");
    });

    $(".hidebox h1").click(function () {
        if(h1_hide == 1) {
            h1_hide = 0
            $(this).next("p").show("slow");
            $(this).css("background-color", "#FFFFFF");
            $(this).css("color", "#212529");
        } else {
            h1_hide = 1;
            $(this).next("p").hide("slow");
            $(this).css("background-color", "#1e1e1e");
            $(this).css("color", "#ffffff");
        }
        
    });

    $(".product-menu button").hover(function () {
        $(this).addClass("active"); }).mouseleave(function () {
        $(this).removeClass("active");
     });

    $('.product-menu button').click(function() {
        $(this).parent().parent().find(".selected").removeClass("selected");
        $(this).addClass("selected");
       var str = $(this).text().toLowerCase();
       $(this).parent().parent().parent().parent().find(".page-header1 span").html(str);
        
      })
    
    $('.form__button').click(function(event) {
        event.preventDefault();
    
        confirm('Отправить отзыв?');
      })

});

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





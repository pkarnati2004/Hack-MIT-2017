$(document).ready(function() {
    alert("Welcome to DJ Tung's!!! Search for a song and add it to the queue")
    $("#suggest").on("click", function() {
        // Dynamic Rows Code

        // Get max row id and set new id
        var newid = 0;
        $.each($("#song-table tr"), function() {
            if (parseInt($(this).data("id")) > newid) {
                newid = parseInt($(this).data("id"));
            }
        });
        newid++;

        var tr = $("<tr></tr>", {
            id: "addr" + newid,
            "data-id": newid
        });

        // loop through each td and create new elements with name of newid
        $.each($("#song-table tbody tr:nth(0) td"), function() {
            var cur_td = $(this);

            var children = cur_td.children();

            // add new td and element if it has a nane
            if ($(this).data("name") != undefined) {
                var td = $("<td></td>", {
                    "data-name": $(cur_td).data("name")
                });

                var c = $(cur_td).find($(children[0]).prop('tagName')).clone().val("");
                c.attr("name", $(cur_td).data("name") + newid);
                c.appendTo($(td));
                td.appendTo($(tr));
            } else {
                var td = $("<td></td>", {
                    'text': $('#song-table tr').length
                }).appendTo($(tr));
            }
        });

        // add delete button and td
        /*
        $("<td></td>").append(
            $("<button class='btn btn-danger glyphicon glyphicon-remove row-remove'></button>")
                .click(function() {
                    $(this).closest("tr").remove();
                })
        ).appendTo($(tr));
        */

        // add the new row
        $(tr).appendTo($('#song-table'));

        $(tr).find("td button.row-remove").on("click", function() {
            $(this).closest("tr").remove();
        });
    });




    // // Sortable Code
    // var fixHelperModified = function(e, tr) {
    //     var $originals = tr.children();
    //     var $helper = tr.clone();

    //     $helper.children().each(function(index) {
    //         $(this).width($originals.eq(index).width())
    //     });

    //     return $helper;
    // };

    // $(".table-sortable tbody").sortable({
    //     helper: fixHelperModified
    // }).disableSelection();

    // $(".table-sortable thead").disableSelection();



    // $("#add_row").trigger("click");
});


// $(document).ready(function() {
//     alert("Hello!!!!!")
//     $("#suggest").on("click", function() {
//         var newid = 0
//         $.each($("#song-table"), function() {
//             if (parseInt($(this).data("id")) > newid) {
//                 newid = parseInt($(this).data("id"));
//             }
//         });
//         newid++;

//         var tr = $("<tr></tr>", {
//             id: "addr" + newid,
//             "data-id": newid
//         });

//         $.each($("#song-table tbody tr:nth(0) td"), function() {
//             var cur_td = $(this)
//             var children = cur_td.children()

//             if ($(this).data("name") != undefined) {
//                 var td = $("<td></td>", {
//                     "data-name": $(cur_td).data("name")
//                 });

//                 var c = $(cur_td).find($(children[0]).prop('tagName')).clone().val("");
//                 c.attr("name", $(cur_td).data("name") + newid);
//                 c.appendTo($(td));
//                 td.appendTo($(tr));
//             } else {
//                 var td = $("<td></td>", {
//                     'text': $('#song-table tr').length
//                 }).appendTo($(tr));
//             }

//         });

//         $(tr).appendTo($('#song-table'));

//         // $(tr).find("td button.row-remove").on("click", function() {
//         //     $(this).closest("tr").remove();
//         // });
//     });
//     $("#suggest").trigger("click");
// });
$(document).ready(function() {
    $("#suggest").on("click", function() {
        var newid = 0
        $.each($("#song-table"), function() {
            if (parseInt($(this).data("id")) > newid) {
                newid = parseInt($(this).data("id"));
            }
        });
        newid++;

        var tr = $("<tr></tr>", {
            id: "addr" + newid,
            "data-id": newid
        });

        $.each($("#song-table tbody tr:nth(0) td"), function() {
            var cur_td = $(this)
            var children = cur_td.children()

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

        $(tr).appendTo($('#song-table'));

        // $(tr).find("td button.row-remove").on("click", function() {
        //     $(this).closest("tr").remove();
        // });
    });
});
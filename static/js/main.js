var csrftoken = $("input[name='csrfmiddlewaretoken']").attr("value")

// Autocomplete
$(".search-field").autocomplete({
    _resizeMenu: function () {
        var ul = this.menu.element;
        ul.outerWidth(this.element.outerWidth());
    },
    autofocus: true,
    source : function (request, response) {
        $.post({
            beforeSend: function(request) {
                    request.setRequestHeader("X-CSRFToken", csrftoken);
                },
            url: "/",
            dataType: "json",
            data: JSON.stringify(request),            
            contentType: "application/json",
            success: function(data){
                response($.map(data,                 
                    function(product){
                    return product.name 
                    }
                  )
                );
            }
        });
    }
});

// Ajax request for saving substitute
$(document).ready(function() {
    originalId = $("#original").attr("data-id")
    $(".save-substitute").click(function(e) {
        e.preventDefault();
        var link = $(this)
        substituteId = link.attr("data-id")
        var data = {"original": originalId, "substitute": substituteId}
        $.post({
            beforeSend: function(request) {
                request.setRequestHeader("X-CSRFToken", csrftoken);
            },
            url: "/my-products/save-substitute/",
            dataType: "json",
            data: JSON.stringify(data),
            success: function(data) {
                $(".modal-title").text(data.title);
                $(".modal-body").text(data.message);
                $("#ajaxModal").modal("show");
            }
        });
    });
});

// Ajax request for deleting substitute
$(document).ready(function() {
    $(".delete-substitute").click(function(e) {
        e.preventDefault();
        var link = $(this)
        substitutionId = link.attr("data-id")
        var data = {"id": substitutionId}
        $.post({
            beforeSend: function(request) {
                request.setRequestHeader("X-CSRFToken", csrftoken);
            },
            url: "/my-products/delete-substitute/",
            dataType: "json",
            data: JSON.stringify(data),
            success: function(data) {
                $(".modal-title").text(data.title);
                $(".modal-body").text(data.message);
                $("#ajaxModal").modal("show");
                $("#substitution-"+substitutionId).addClass("d-none").removeClass("d-flex");
            }
        });
    });
});

// Filter for my_products page
$(document).ready(function() {
    $("#showOriginals").click(function () {
        $("#showSubstitutes").attr("disabled", false);
        $("#showOriginals").attr("disabled", true);
        $("#substitutes").addClass('d-none').removeClass('d-flex');
        $('#originals').addClass('d-flex').removeClass('d-none');
        $("#listTitle").text("Mes produits recherchés");        
    });
    $("#showSubstitutes").click(function () {
        $("#showSubstitutes").attr("disabled", true);
        $("#showOriginals").attr("disabled", false);
        $("#originals").addClass('d-none').removeClass('d-flex');
        $('#substitutes').addClass('d-flex').removeClass('d-none');
        $("#listTitle").text("Mes produits enregistrés");
    });
});
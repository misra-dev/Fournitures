function getCategory(id){
    console.log("id " + id);

  var url = `/backend/get_cat/${id}/`;
    console.log("url " + url);

    $.ajax({
        url: url,
        type: 'GET',
        success: function(data){
            console.log(data);
            console.log($("#editCat"))

            $("input[name='cat_name']").val(data.cat_name)
            $("input[name='id']").val(id)

            $("#editCat").modal('toggle')
            $("#editCat").modal('show')

        },
        error: function(xhr, textStatus, errorThrown) {
            console.log('Erreur lors de la récupération des données:', errorThrown);
        }
    });
}
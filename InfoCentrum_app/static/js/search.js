$(function(){

var input = $('input');
console.log(input);

$('#result').on("click", function(event){
  console.log(event.target);
});


function delete_not_checked(){
    var result = $('#result');
    result.children().each(function(index, value){
        //console.log($(value).prop('checked'));
        if($(value).children().first().prop('checked') == false) {
            $(value).remove();
        }
    });
}

function add_if_not_exists(value){
    var result = $('#result');
    console.log(result.children());
    for(var i=0; i < result.children().length; i++){
        if (result.children().eq(i).data('id') == value.id)
        {
            return null;
        }
    }
    result.append(`<span data-id=${value.id}><input type='checkbox' value='${value.id}' name='purpose'>${value.purpose}</span>`);
}


input.on("keyup", function(event){
   console.log($(this).val());
   if($(this).val().length > 2)
   {
        $.ajax({
          url:
          "/search_purpose/" + $(this).val() + "/",
          dataType: "json",
        }).done(function(data) {
          //$('#result').text(data);
            delete_not_checked();
          $(data).each(function(index, value){

           //  $('#result').append(`<input type='checkbox' value='${value.id}'>${value.purpose}`);
             add_if_not_exists(value);
          });
        });
    }
    else
    {
      //  $('#result').text("");
     delete_not_checked();
    }
    });


});
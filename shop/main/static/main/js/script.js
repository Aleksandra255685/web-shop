$(document).ready(function(){
    var form = $('#form_buying');
    console.log(form);
    form.on('submit', function(e){
        e.preventDefault();
        console.log('123');
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var product_id =  submit_btn.data("product_id");
        var name = submit_btn.data("name");
        var price = submit_btn.data("price");
        console.log(product_id );
        console.log(name);

        var data={};
        data.product_id = product_id;
        data.nmb = nmb;
        var csrf_token = $('#form_buying [name="csrfmiddlewaretoken"]').val();
        data['csrfmiddlewaretoken'] = csrf_token
        var url = form.attr("action");
        $.ajax({
            url: url,
            type: 'POST'
            data: data,
            cache: true,
            success: function(data){
               console.log('OK')
               if (data.products_total_nmb){

                   $('.basket-items ul').html("");
                   $.each(data.products, function(k, v){
                       $('.basket-items ul').append('<li>'+ v.name+', ' + v.nmb + ' кг. ' + v.price_per_item + ' ₽/кг  ' +
                       '</li>');
                   })
               }
            }
        })
    });

     $(document).on('click', '.delete-item', function(e){
         e.preventDefault();
         $(this).closest('li').remove();
     })

});
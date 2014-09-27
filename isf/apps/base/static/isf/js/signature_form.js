$(function()
{
    $.ajaxSetup({ 
         beforeSend: function(xhr, settings) {
             function getCookie(name) {
                 var cookieValue = null;
                 if (document.cookie && document.cookie != '') {
                     var cookies = document.cookie.split(';');
                     for (var i = 0; i < cookies.length; i++) {
                         var cookie = jQuery.trim(cookies[i]);
                         // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
             }
             if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                 // Only send the token to relative URLs i.e. locally.
                 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
             }
         } 
    });

    $("input,textarea").jqBootstrapValidation({
        preventSubmit: true,
        submitError: function($form, event, errors)
        {
            // additional error messages or events
        },
        submitSuccess: function($form, event)
        {
            event.preventDefault(); // prevent default submit behaviour
            
            var data = $form.serialize();

            $.ajax({
                url: url,
                type: "POST",
                data: data,
                cache: false,
                dataType: "json",
                success: function(data)
                {
                    if (typeof data.errors == 'undefined')
                    {
                        // add name
                        var name = data[0].fields.name;
                        var html = '<p class="person col-lg-3 col-lg-offset-1">' + name + '</p>'
                        $('.people .list').append(html);

                        // Success message
                        $('#success').html("<div class='alert alert-success'>");
                        $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
                            .append("</button>");
                        $('#success > .alert-success')
                            .append("Your signature has been sent.");
                        $('#success > .alert-success')
                            .append('</div>');

                        //clear all fields
                        $('#signForm').trigger("reset");                        
                    }
                    else
                    {
                        error_callback(data);
                    }


                },
                error: function(data)
                {
                    error_callback(data);
                },
            })
        },
        filter: function() {
            return $(this).is(":visible");
        },
    });

    $("a[data-toggle=\"tab\"]").click(function(e) {
        e.preventDefault();
        $(this).tab("show");
    });
});

function error_callback(data)
{
    var error_message = (data.errors) ? data.errors[0] : "Sorry, something went wrong!";
    
    // Fail message
    $('#success').html("<div class='alert alert-danger'>");
    $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
        .append("</button>");
    $('#success > .alert-danger').append(error_message);
    $('#success > .alert-danger').append('</div>');
    //clear all fields
    $('#signForm').trigger("reset");    
}


/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
    $('#success').html('');
});

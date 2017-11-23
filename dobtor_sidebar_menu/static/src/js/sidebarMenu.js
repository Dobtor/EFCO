$(function () {
    console.log('test');
    $('.icon_width input').attr('type', 'number');
    $(document).on('DOMNodeInserted', '.icon_width', function() {
        $('.icon_width').find('input').attr('type', 'number');
        
        $('.icon_width input').find('input').on('input', function () {
            var val = $(this).val()
            console.log(val)
            if (!isNaN(Number(val))) {
                console.log(val)
                if (Number(val) < 256) {
                    $('img[name="icon_img"]').css('width', val)
                    console.log(val)
                }
            }
        })  
    })
    
})


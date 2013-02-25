/**
 * Author: Samuel M.H. <samuel.mh@gmail.com>
 *
 * Date: 13-Feb-2013
 *
 * Description:
 *  Javascript library that converts .img_color-gray class images to
 *   grayscale with increased contrast and when the mouse is over colors them
 *   again.
 *
 */


$(window).load(function(){

    $('.img_color-gray').each(
        function(){
            var img_gray = this; //Will be grayscaled
            $(img_gray).clone().addClass('img_color').insertBefore(img_gray);
            $(img_gray).addClass('img_gray');
            img_gray.src = grayscale(img_gray.src);
            var img_color = $(img_gray).parent().find('.img_color')[0];
            copy_style(img_gray, img_color);
            $(img_color).css({"opacity":"1"}); //Avoid blink
        }
    );

    //Avoid blink
    $('.img_color').each(
        function(){
            $(this).animate({opacity:0}, 2000);
        }
    );

    $('.img_color').mouseover(
        function(){
            $(this).stop().animate({opacity:1}, 1000);
        });

    $('.img_color').mouseout(
        function(){
            $(this).stop().animate({opacity:0}, 1000);
        }
    );

});


//Responsive
$(window).resize(function() {
    $('.img_color').each(
        function(){
            var img_gray = $(this).parent().find('.img_gray')[0];
            copy_style(img_gray, this);
        }
    );
});



function copy_style(origin, destiny){
        $(destiny).css({"position":"absolute","z-index":"998","opacity":"0"});
        $(destiny).css({"position":"absolute","width":origin.offsetWidth,"height":origin.offsetHeight});
        $(destiny).offset($(origin).offset());
}


// Grayscale w canvas method
function grayscale(src){
    var canvas = document.createElement('canvas');
    var ctx = canvas.getContext('2d');
    var imgObj = new Image();
    imgObj.src = src;
    canvas.width = imgObj.width;
    canvas.height = imgObj.height;
    ctx.drawImage(imgObj, 0, 0);
    var imgPixels = ctx.getImageData(0, 0, canvas.width, canvas.height);
    for(var y = 0; y < imgPixels.height; y++){
        for(var x = 0; x < imgPixels.width; x++){
            var i = (y * 4) * imgPixels.width + x * 4;
            var avg = ((imgPixels.data[i] + imgPixels.data[i + 1] + imgPixels.data[i + 2]) /2) - 32  ;
            imgPixels.data[i] = avg;
            imgPixels.data[i + 1] = avg;
            imgPixels.data[i + 2] = avg;
        }
    }
    ctx.putImageData(imgPixels, 0, 0, 0, 0, imgPixels.width, imgPixels.height);
    return canvas.toDataURL();
}
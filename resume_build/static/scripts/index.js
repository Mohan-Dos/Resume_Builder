$(document).ready(function() {
    $('.content').waypoint(function(){
        $('.content').addClass('animate__animated onopacity animate__zoomIn')
    }, {offset: '50%'})

    // resume images 

    $('.resume_img').waypoint(function(){
        $('.resume_img').addClass('animate__animated onopacity animate__fadeInRight')
    }, {offset: '50%'})

    $('.resume_img2').waypoint(function(){
        $('.resume_img2').addClass('animate__animated onopacity animate__fadeInRight')
    }, {offset: '50%'})

    // features tittle

    $('.features_tittle').waypoint(function(){
        $('.features_tittle').addClass('animate__animated onopacity animate__zoomIn')
    }, {offset: '80%'})

    // features 1st row

    $('.one').waypoint(function(){
        $('.one').addClass('animate__animated onopacity animate__zoomIn')
    }, {offset: '80%'})

    $('.two').waypoint(function(){
        $('.two').addClass('animate__animated onopacity animate__zoomIn')
    }, {offset: '80%'})

    // line

    $('.horiz').waypoint(function(){
        $('.horiz').addClass('animate__animated onopacity animate__zoomIn')
    }, {offset: '50%'})


    // temp title
    
    $('.temp_title').waypoint(function(){
        $('.temp_title').addClass('animate__animated onopacity animate__zoomIn')
    }, {offset: '80%'})

    // template images

    $('.img1').waypoint(function(){
        $('.img1').addClass('animate__animated onopacity animate__fadeInRight')
    }, {offset: '60%'})

    $('.img2').waypoint(function(){
        $('.img2').addClass('animate__animated onopacity animate__fadeInRight')
    }, {offset: '60%'})

    $('.img3').waypoint(function(){
        $('.img3').addClass('animate__animated onopacity animate__fadeInRight')
    }, {offset: '60%'})

    $('.img4').waypoint(function(){
        $('.img4').addClass('animate__animated onopacity animate__fadeInRight')
    }, {offset: '60%'})

    $('.img5').waypoint(function(){
        $('.img5').addClass('animate__animated onopacity animate__fadeInRight')
    }, {offset: '60%'})


    
});
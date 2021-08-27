$(document).ready(function() {
    $('a.abstract').click(function() {
        $(this).parent().parent().find(".abstract.hidden").toggleClass('open');
    });
    $('a.bibtex').click(function() {
        $(this).parent().parent().find(".bibtex.hidden").toggleClass('open');
    });
    $('.navbar-nav').find('a').removeClass('waves-effect waves-light');
    $(".sports").mouseover(function (){
        $(document).find(".profile").children('img').attr('src', '/assets/img/prof_pic_flu.jpg');
    });
    $(".sports").mouseout(function (){
        console.log("out");
        $(document).find(".profile").children('img').attr('src', '/assets/img/prof_pic.jpg');
    });
});

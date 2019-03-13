$(document).ready(function(){
                $('.single-item').slick({
                autoplay: true,
                dots: true,
                infinite: true,
                arrows: false,
                centerMode: true
                    });
                });


                $(document).ready(function(){
                    $('.collapsible').collapsible();
                    $('select').material_select();
                    $(".button-collapse").sideNav();
                 });


                            $('a.twitter').confirm({
                                content: "...",
                                    });
                                    $('a.twitter').confirm({
                                buttons: {
                    hey: function(){
            location.href = this.$target.attr('href');
        }
    }
});

       

                            var elems = document.getElementsByClassName('confirm');
                            var confirmIt = function (e) {
                                if (!confirm('Are you sure? This action cannot be undone!')) e.preventDefault();
                                    };
                                for (var i = 0, l = elems.length; i < l; i++) {
                                elems[i].addEventListener('click', confirmIt, false);
                                    }

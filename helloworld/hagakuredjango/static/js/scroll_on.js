//scroll_effect
  $(function(){

  });

  $(window).on('load scroll', function(){
    scroll_up_animation(-50);
  });

  function scroll_up_animation(triggerMargin){
    var scrollAnimationElm = document.querySelectorAll('.scroll_up');

    // console.log("animation")

      for (var i = 0; i < scrollAnimationElm.length; i++) {
        // console.log("No.:" + i + ", top:" + scrollAnimationElm[i].getBoundingClientRect().top + ", height:" + window.innerHeight);
        if (window.innerHeight > scrollAnimationElm[i].getBoundingClientRect().top + triggerMargin) {
          scrollAnimationElm[i].classList.add('on');
        }
      }
  }
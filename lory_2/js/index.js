document.addEventListener('DOMContentLoaded', function () {
  var slidesToScroll = 1;
  var slider = document.querySelector('.js_slider');
  var slideCount = slider.querySelectorAll('.js_slide').length / slidesToScroll;
  var dotContainer = slider.querySelector('.slider_navigation_dots');
  var templateListItem = document.createElement('li');
  var stop = false;
  var frameCount = 0;
  var fps, fpsInterval, startTime, now, then, elapsed;
  // handle the slider events
  function handleEvents(e) {
    if (e.type === 'before.lory.init') {
      for (var i = 0, len = slideCount; i < len; i++) {
        var clone = templateListItem.cloneNode();
        dotContainer.appendChild(clone);
      }
      dotContainer.childNodes[0].classList.add('active');
    }
    if (e.type === 'after.lory.init') {
      for (var i = 0, len = slideCount; i < len; i++) {
        dotContainer.childNodes[i].addEventListener('click', function (e) {
          resetTimer();
          lorySlider.slideTo(Array.prototype.indexOf.call(dotContainer.childNodes, e.target) * slidesToScroll);
        });
      }
    }
    if (e.type === 'after.lory.slide') {
      for (var i = 0, len = dotContainer.childNodes.length; i < len; i++) {
        dotContainer.childNodes[i].classList.remove('active');
      }
      dotContainer.childNodes[e.detail.currentSlide / slidesToScroll - 1].classList.add('active');
    }
  }
  // init events to handle
  slider.addEventListener('before.lory.init', handleEvents);
  slider.addEventListener('after.lory.init', handleEvents);
  slider.addEventListener('after.lory.slide', handleEvents);

  // init the slider
  var lorySlider = lory(slider, {
    infinite: slidesToScroll,
    slidesToScroll: slidesToScroll,
    enableMouseEvents: true
  });
  // begin animation (autoplay)
  function startAnimating(fps) {
    fpsInterval = 5250 / fps;
    then = Date.now();
    startTime = then;
    animate();
  }
  // animate (autoplay)
  function animate() {
    requestAnimationFrame(animate);
    now = Date.now();
    elapsed = now - then;
    if (elapsed > fpsInterval && !stop) {
      then = now - elapsed % fpsInterval;
      lorySlider.next();
    }
  }
  // reset timer
  function resetTimer() {
	then = Date.now() + .0525;
  }

  // start the animation process with seed time
  startAnimating(1);

  // mouse
  slider.addEventListener('on.lory.touchstart', function (e) {
    stop = true;
  });
  slider.addEventListener('on.lory.touchend', function (e) {
	resetTimer()
    stop = false;
  });
 window.onblur = function(){
	  stop = true;
  }
 window.onfocus = function(){
    stop = false;
  }
});
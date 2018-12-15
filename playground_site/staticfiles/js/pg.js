$( document ).ready(function() {
  console.log( "ready!" );
  const reveals = Array.from(document.querySelectorAll(".fall"));

  const DELAY_PER_ITEM = 200;
  const DEFER_PIXELS = 200;
  let lastScrollPos = 0;
  let ticking = false;

  const check = scrollPos => {
    const found = [];
    reveals.forEach(item => {
    	const itemY = item.offsetTop;
      if (itemY < scrollPos + window.innerHeight - DEFER_PIXELS && !item.seen) {
        found.push(item);
      }
    });
    let i = 0;
    found.forEach(item => {
    	item.seen = true;
    	setTimeout(() => {
        item.classList.add("animate");
      }, DELAY_PER_ITEM * i++);
    });
  };

  window.addEventListener('scroll', e => {
    lastScrollPos = window.scrollY;
    if (!ticking) {
      window.requestAnimationFrame(() => {
        check(lastScrollPos);
        ticking = false;
      });
      ticking = true;
    }
  });

  check(0);
});

// Minimal replacement for Bootstrap's collapse plugin (navbar toggler, FAQ accordion).
// Uses Bootstrap's CSS classes: .collapse, .show, .collapsing (animates height).
(() => {
  const transitionMs = 350; // $transition-collapse in Bootstrap
  const triggersFor = (target) =>
    document.querySelectorAll(`[data-bs-toggle="collapse"][data-bs-target="#${target.id}"]`);

  const setExpanded = (target, expanded) => {
    if (target.classList.contains('collapsing') || target.classList.contains('show') === expanded) {
      return;
    }

    triggersFor(target).forEach((trigger) => {
      trigger.classList.toggle('collapsed', !expanded);
      trigger.setAttribute('aria-expanded', String(expanded));
    });

    if (expanded) {
      target.classList.remove('collapse');
      target.classList.add('collapsing');
      target.style.height = '0px';
      target.offsetHeight; // Force reflow so the height transition starts from 0
      target.style.height = `${target.scrollHeight}px`;
    } else {
      target.style.height = `${target.getBoundingClientRect().height}px`;
      target.offsetHeight; // Force reflow so the height transition starts from the current height
      target.classList.add('collapsing');
      target.classList.remove('collapse', 'show');
      target.style.height = '';
    }

    // A timeout instead of transitionend, which never fires with prefers-reduced-motion
    setTimeout(() => {
      target.classList.remove('collapsing');
      target.classList.add('collapse');
      target.classList.toggle('show', expanded);
      target.style.height = '';
    }, transitionMs);
  };

  document.addEventListener('click', (event) => {
    const trigger = event.target.closest('[data-bs-toggle="collapse"]');
    if (!trigger) {
      return;
    }
    event.preventDefault();

    const target = document.querySelector(trigger.dataset.bsTarget);
    if (!target) {
      return;
    }

    const expand = !target.classList.contains('show');
    const parent = target.dataset.bsParent && document.querySelector(target.dataset.bsParent);
    if (expand && parent) {
      parent.querySelectorAll('.collapse.show').forEach((open) => setExpanded(open, false));
    }
    setExpanded(target, expand);
  });
})();

// "Smart" navbar from startbootstrap-clean-blog
window.addEventListener('DOMContentLoaded', () => {
  let scrollPos = 0;
  const mainNav = document.getElementById('mainNav');
  const headerHeight = mainNav.clientHeight;
  window.addEventListener('scroll', function () {
    if (window.innerWidth < 1200) {
      return;
    }
    const currentTop = document.body.getBoundingClientRect().top * -1;
    if (currentTop < scrollPos) {
      // Scrolling Up
      if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
        mainNav.classList.add('is-visible');
      } else {
        mainNav.classList.remove('is-visible', 'is-fixed');
      }
    } else {
      // Scrolling Down
      mainNav.classList.remove(['is-visible']);
      if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
        mainNav.classList.add('is-fixed');
      }
    }
    scrollPos = currentTop;
  });
})

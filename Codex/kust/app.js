document.querySelectorAll('[data-comparison]').forEach((input) => {
  const comparison = input.closest('.comparison');
  input.addEventListener('input', () => {
    comparison.style.setProperty('--position', `${input.value}%`);
    input.setAttribute('aria-valuetext', `${input.value} procent van het vóór-beeld zichtbaar`);
  });
});

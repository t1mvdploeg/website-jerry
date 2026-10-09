document.querySelectorAll('[data-comparison]').forEach((input) => {
  const comparison = input.closest('.comparison');
  input.addEventListener('input', () => {
    comparison.style.setProperty('--position', `${input.value}%`);
    input.setAttribute('aria-valuetext', `${input.value} procent van het vóór-beeld zichtbaar`);
  });
});

document.querySelectorAll('[data-offerte]').forEach((helper) => {
  const link = document.querySelector('[data-offerte-link]');
  const preview = helper.querySelector('[data-offerte-bericht]');
  const chosen = (name) => helper.querySelector(`input[name="${name}"]:checked`)?.closest('label').textContent.trim();
  const update = () => {
    const lines = ['Hallo, ik wil graag een vrijblijvende offerte.'];
    for (const [label, name] of [['Klus', 'klus'], ['Plaats', 'plaats'], ['Wanneer', 'wanneer']]) {
      if (chosen(name)) lines.push(`${label}: ${chosen(name)}`);
    }
    lines.push('Ik stuur foto’s mee.');
    preview.textContent = lines.join('\n');
    link.href = `https://wa.me/31621193640?text=${encodeURIComponent(lines.join('\n'))}`;
  };
  helper.hidden = false;
  helper.addEventListener('change', update);
  update();
});

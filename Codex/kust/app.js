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

document.querySelectorAll('[data-werk-stappen]').forEach((steps) => {
  const photo = steps.parentElement.querySelector('[data-werk-img]');
  steps.hidden = false;
  steps.addEventListener('click', (event) => {
    const button = event.target.closest('button');
    if (!button || button.getAttribute('aria-pressed') === 'true') return;
    steps.querySelectorAll('button').forEach((b) => b.setAttribute('aria-pressed', b === button));
    photo.classList.add('is-wissel');
    photo.onload = photo.onerror = () => photo.classList.remove('is-wissel');
    photo.src = button.dataset.src;
    photo.alt = button.dataset.alt;
  });
});

document.querySelectorAll('[data-werk-filter]').forEach((filter) => {
  const jobs = filter.parentElement.querySelectorAll('.werk');
  filter.hidden = false;
  filter.addEventListener('click', (event) => {
    const button = event.target.closest('button');
    if (!button) return;
    filter.querySelectorAll('button').forEach((b) => b.setAttribute('aria-pressed', b === button));
    jobs.forEach((job) => { job.hidden = Boolean(button.dataset.dienst) && job.dataset.dienst !== button.dataset.dienst; });
  });
});

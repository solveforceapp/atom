// Simple site scripts: mobile nav toggle + contact form stub
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.getElementById('nav-toggle');
  var nav = document.getElementById('main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
      toggle.classList.toggle('open');
    });
  }
});

function submitContact(e) {
  if (e) e.preventDefault();
  var status = document.getElementById('form-status');
  if (!status) return false;
  status.textContent = 'Sending message… (this demo does not send mail)';
  // In a real site, send via fetch() to an API endpoint here.
  setTimeout(function () {
    status.textContent = 'Thanks — we received your message. We will reply within 2 business days.';
    document.getElementById('contact-form')?.reset();
  }, 900);
  return false;
}
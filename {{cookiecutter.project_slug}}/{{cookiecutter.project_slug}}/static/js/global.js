{% raw %}
const tooltipTriggerList =
      [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));

const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});

const csrfToken = document.currentScript.getAttribute('csrf');
const debug = document.currentScript.getAttribute('debug');

document.body.addEventListener('htmx:configRequest', (event) => {
  event.detail.headers['X-CSRFToken'] = csrfToken;
});

if (debug) {
  document.addEventListener("DOMContentLoaded", function(event) {
    htmx.logger = function(elt, event, data) {
      if(console) {
        console.debug(event, elt, data);
      }
    };
  });
}
{%- endraw %}

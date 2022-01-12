function loadTooltips() {
  const tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
  );

  const tooltipList = tooltipTriggerList
        .map(function (tooltipTriggerEl) {
          return new bootstrap.Tooltip(tooltipTriggerEl);
        });
}

function loadHtmx() {
  // TODO only load this when DEBUG=1
  document.addEventListener("DOMContentLoaded", function(event) {
    htmx.logger = function(elt, event, data) {
      if(console) {
        console.debug(event, elt, data);
      }
    };
  });

  document.body.addEventListener('htmx:configRequest', (event) => {
    event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
  });
}

loadTooltips();
loadHtmx();

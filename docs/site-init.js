(function () {
  var config = window.SITE_CONFIG || {};
  var key = (config.web3formsAccessKey || "").trim();
  var siteUrl = (config.siteUrl || "").replace(/\/$/, "");
  var propertyName = config.propertyName || "Ganga Residency";
  var placeholderKey = "YOUR_WEB3FORMS_ACCESS_KEY";
  var uuidPattern =
    /^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
  var hasValidKey = key && key !== placeholderKey && uuidPattern.test(key);

  if (!hasValidKey) {
    console.warn(
      "[Ganga Residency] Form not configured: set web3formsAccessKey in site-config.js. Get a free key at https://web3forms.com"
    );
  }

  document.querySelectorAll('form[action*="web3forms.com"]').forEach(function (form) {
    var access = form.querySelector('input[name="access_key"]');
    if (access && hasValidKey) {
      access.value = key;
    }

    var subject = form.querySelector('input[name="subject"]');
    if (subject) {
      subject.value = config.formSubject || propertyName + " Website Lead";
    }

    var fromName = form.querySelector('input[name="from_name"]');
    if (fromName) {
      fromName.value = config.formFromName || propertyName + " Website";
    }

    var messageField = form.querySelector('[name="message"]');
    if (messageField && messageField.tagName === "INPUT" && !messageField.value) {
      messageField.value =
        config.formDefaultMessage ||
        "Interested in " + propertyName + " - Site Visit";
    }

    var redirect = form.querySelector('input[name="redirect"]');
    if (!redirect) {
      redirect = document.createElement("input");
      redirect.type = "hidden";
      redirect.name = "redirect";
      form.appendChild(redirect);
    }
    if (siteUrl && siteUrl.indexOf("YOUR_USERNAME") === -1) {
      redirect.value = siteUrl + "/thank-you.html";
    } else {
      redirect.value = "thank-you.html";
    }

    form.addEventListener("submit", function (event) {
      if (hasValidKey) {
        return;
      }

      event.preventDefault();
      alert(
        "Online form is not active yet. Please call +91-9650655124 or WhatsApp us for Ganga Residency enquiries."
      );
    });
  });
})();

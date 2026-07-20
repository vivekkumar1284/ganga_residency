(function () {
  var config = window.SITE_CONFIG || {};
  var key = config.web3formsAccessKey || "";
  var siteUrl = (config.siteUrl || "").replace(/\/$/, "");

  document.querySelectorAll('form[action*="web3forms.com"]').forEach(function (form) {
    var access = form.querySelector('input[name="access_key"]');
    if (access && key && key !== "YOUR_WEB3FORMS_ACCESS_KEY") {
      access.value = key;
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
  });
})();

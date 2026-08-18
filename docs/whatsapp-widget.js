(function () {
  var config = window.SITE_CONFIG || {};
  var propertyName = config.propertyName || "Ganga Residency";

  var wa_btnSetting = {
    btnColor: "#16BE45",
    ctaText: "WhatsApp Us",
    cornerRadius: 40,
    marginBottom: 16,
    marginLeft: 20,
    marginRight: 20,
    btnPosition: "left",
    whatsAppNumber: config.whatsappNumber || "919650655124",
    welcomeMessage:
      config.whatsappWelcomeMessage ||
      "Get More Details About " + propertyName,
    zIndex: 999999,
    btnColorScheme: "light",
  };

  function embedWidget() {
    if (typeof window._waEmbed === "function") {
      window._waEmbed(wa_btnSetting);
    }
  }

  window.onload = embedWidget;
  window.addEventListener("pageshow", function (event) {
    if (event.persisted) {
      embedWidget();
    }
  });
})();

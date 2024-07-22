import Cookify from "/assets/js/cookify/index.js";

function handle_cookies() {
  var cookieModal = document.getElementById("cookieBanner");
  var cookify = new Cookify(
    "cookie_consent",
    function () {
      cookieModal.style.display = "none";
    },
    function (data) {
      console.log(data);
      if (data[0].statistics) {
        gtag("consent", "update", {
          analytics_storage: "granted",
        });
      }
      if (data[0].marketing) {
        gtag("consent", "update", {
          ad_user_data: "granted",
          ad_personalization: "granted",
          ad_storage: "granted",
        });
      }
    },
    false,
    false,
    "necessary"
  );

  if (!cookify.getDataState(cookify.viewedName)) {
    cookieModal.style.display = "block";
  } else {
    if (cookify.getDataState("statistics")) {
      gtag("consent", "update", {
        analytics_storage: "granted",
      });
    }
    if (cookify.getDataState("marketing")) {
      gtag("consent", "update", {
        ad_user_data: "granted",
        ad_personalization: "granted",
        ad_storage: "granted",
      });
    }
  }
}
window.addEventListener("load", handle_cookies);

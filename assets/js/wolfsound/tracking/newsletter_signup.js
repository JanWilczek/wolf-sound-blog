jQuery(function () {
    subscribeButton = $("#mc-embedded-subscribe");
    if (subscribeButton != null) {
        subscribeButton.on("click", function () {
            gtag("event", "newsletter_sidebar_sign_up_button_clicked", {
                "event_category": "newsletter_sign_up",
                "event_label": location.pathname
            }
            );
        });
    }
});

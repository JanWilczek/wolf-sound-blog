import Cookify from '/assets/js/cookify/index.js'
    function handle_cookies(){
        var cookieModal = document.getElementById("cookieBanner")
        var cookify = new Cookify('cookie_consent', function () {
            cookieModal.style.display = "none";
        }, function (data) {
            console.log(data)
        }, false, false, 'necessary')

        if (!cookify.getDataState(cookify.viewedName)) {
            cookieModal.style.display = "block"
        }  
    }
    window.addEventListener('load', handle_cookies)
    
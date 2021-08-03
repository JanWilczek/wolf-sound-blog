import Cookify from '/assets/js/cookify/index.js'
    function handle_cookies(){
        var cookieModal = document.getElementById("cookieModal")
        var cookify = new Cookify('cookie_consent', function () {
            // document.getElementById('manage').classList.add('d-none')
            cookieModal.style.display = "none";
        }, function (data) {
            console.log(data)
        }, false, false, 'necessary')

        if (!cookify.getDataState(cookify.viewedName)) {
            // document.getElementById('manage').classList.remove('d-none')
            cookieModal.style.display = "block"
        }  
    }
    window.addEventListener('load', handle_cookies)
    
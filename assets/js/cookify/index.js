export default class Cookify {
    constructor(dataName = 'cookify', actionCallback = () => {}, trackingCallback = () => {}, saveWithChange = false, saveByDefault = false, cookieDefault = 'necessary') {
        this.dataName = dataName
        this.data = new Object
        this.query = 'data-c-'
        this.trackingCallback = trackingCallback
        this.saveByDefault = saveByDefault
        this.saveWithChange = saveWithChange
        this.cookieDefault = cookieDefault
        this.viewedName = 'viewed'
        this.actionCallback = actionCallback

        this.init()
    }

    init() {
        this.initData()

        this.initCheckboxes()

        this.initListeners()
    }

    /**
     * Check the data for integrity
     */
    initData() {
        if (!this.getMemoryData()) {
            var typeElements = document.querySelectorAll('input' + this.getQueryDataBrackets('check'))
            
            for (const typeElement of typeElements) {
                if (typeElement.getAttribute(this.getQueryData('check')) == this.cookieDefault || typeElement.getAttribute(this.getQueryData('check-default')) == 'true') {
                    this.data[typeElement.getAttribute(this.getQueryData('check'))] = true
                } else {
                    this.data[typeElement.getAttribute(this.getQueryData('check'))] = false
                }
            }

            this.data[this.viewedName] = false
            this.saveByDefault ? this.setMemoryData(this.data) : null
        } else {
            this.data = this.getMemoryData()
        }
    }

    /**
     * Initialize the checkboxes
     */
    initCheckboxes() {
        var typeElements = document.querySelectorAll('input' + this.getQueryDataBrackets('check'))

        for (const typeElement of typeElements) {
            var type = typeElement.getAttribute(this.getQueryData('check'))

            if (this.getDataState(type)) {
                var checkboxElements = document.querySelectorAll('input' + this.getQueryDataBrackets('check', type))

                for (const checkboxElement of checkboxElements) {
                    checkboxElement.checked = 'checked'

                    if (type == this.cookieDefault) {
                        checkboxElement.disabled = true
                    }
                }

                this.changeScriptType(type, 'js')
            }
        }
    }

    /**
     * Initialize the Listeners
     */
    initListeners() {
        // Checkboxes
        var checkboxElements = document.querySelectorAll('input' + this.getQueryDataBrackets('check'))

        for (const checkboxElement of checkboxElements) {
            checkboxElement.addEventListener('click', this.onCheckboxClick)
        }

        // Actions
        var actionElements = document.querySelectorAll(this.getQueryDataBrackets('action'))

        for (const actionElement of actionElements) {
            switch (actionElement.getAttribute(this.getQueryData('action'))) {
                case 'accept':
                    actionElement.addEventListener('click', this.onActionAcceptClick)
                    break;

                case 'necessary':
                    actionElement.addEventListener('click', this.onActionNecessaryClick)
                    break;

                case 'all':
                    actionElement.addEventListener('click', this.onActionAllClick)
                    break;
            
                default:
                    break;
            }
        }
    }

    /**
     * Get the query name for selecting elements
     * 
     * @param {string} type 
     * @param {string} element 
     * @returns {string}
     */
    getQueryData(type, element = '') {
        return element == '' ? `${this.query}${type}` : `${this.query}${type}="${element}"`
    }

    /**
     * Get the query name with brackets for selecting elements
     * 
     * @param {string} type 
     * @param {string} element 
     * @returns {string}
     */
    getQueryDataBrackets(type, element = '') {
        return '[' + this.getQueryData(type, element) + ']'
    }

    /**
     * Read the saved data
     * 
     * @returns data
     */
    getMemoryData() {
        // Get from Cookies
        var name = this.dataName + '=',
            ca = document.cookie.split(';')

        for(var i = 0; i < ca.length; i++) {
            var c = ca[i]

            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return JSON.parse(atob(c.substring(name.length, c.length)))
            }
        }

        return false
    }

    /**
     * Set the data
     * 
     * @param data
     */
    setMemoryData(data) {
        // Callback for tracking user activity
        this.trackingCallback([
            data,
            new Date()
        ])

        // Verschlüsselung
        data = btoa(JSON.stringify(data))

        // Save in cookies
        var date = new Date(),
            expire = 365,
            expires = ''

        date.setTime(date.getTime() + (expire * 24 * 60 * 60 * 1000))
        expires = 'expires=' + date.toUTCString()
        document.cookie = this.dataName + '=' + data + ';' + expires + ';path=/;secure'
    }

    /**
     * Get a cookie state
     * 
     * @param {string} type 
     */
    getDataState(type) {
        for (const key in this.data) {
            if (key == type) {
                return this.data[key] === true
            }
        }

        return false
    }

    /**
     * Changes the cookie state and saves the data
     * 
     * @param {string} type 
     * @param {boolean} value 
     * @returns {boolean} 
     */
    changeDataState(type, value) {
        for (const key in this.data) {
            if (key == type) {
                this.data[key] = value
            }
        }

        this.saveWithChange ? this.setMemoryData(this.data) : null

        // Call Event to let the user track activity
        return value
    }

    /**
     * Any Script type can be changed from text/plain
     * and text/javascript and back
     * 
     * @param {string} script 
     * @param {string} type 
     */
    changeScriptType(script, type) {
        var scriptElements = document.querySelectorAll('script' + this.getQueryDataBrackets('script'))

        for (const scriptElement of scriptElements) {
            if (scriptElement.getAttribute(this.getQueryData('script')) == script) {
                if (type == 'js') {
                    scriptElement.setAttribute('type', 'text/javascript')

                    if (scriptElement.hasAttribute("src")) {
                        scriptElement.setAttribute("src", scriptElement.getAttribute("src"))
                    } else {
                        scriptElement.innerHTML = scriptElement.innerHTML
                    }
                } else {
                    scriptElement.setAttribute('type', 'text/plain')
                }
            }
        }
    }

    /**
     * Event Listeners
     */

    /**
     * Event on mouse click
     * 
     * @param {event} e 
     */
    onCheckboxClick = e => {
        var type = e.target.getAttribute(this.getQueryData('check')),
            checkboxElements = document.querySelectorAll('input' + this.getQueryDataBrackets('check', type)),
            cookieState = this.getDataState(type)

        cookieState = this.changeDataState(type, !cookieState)
        cookieState && this.saveWithChange ? this.changeScriptType(type, 'js') : this.changeScriptType(type, 'plain')

        for (const checkboxElement of checkboxElements) {
            cookieState ? checkboxElement.checked = 'checked' : checkboxElement.checked = false
        }
    }

    /**
     * Event on action accept click
     */
    onActionAcceptClick = () => {
        for (const type in this.data) {
            if (type != this.viewedName) {
                this.data[type] ? this.changeScriptType(type, 'js') : this.changeScriptType(type, 'plain')
            }
        }
        
        this.data[this.viewedName] = true
        this.setMemoryData(this.data)
        this.actionCallback()
    }

    /**
     * Event action accept only necessary click
     */
    onActionNecessaryClick = () => {
        // Nur notwendig auf true
        for (const type in this.data) {
            if (type != this.cookieDefault && type != this.viewedName) {
                this.data[type] = false
                this.changeScriptType(type, 'plain')

                var checkboxElements = document.querySelectorAll('input' + this.getQueryDataBrackets('check', type))

                for (const checkboxElement of checkboxElements) {
                    checkboxElement.checked = false
                }
            }
        }

        this.data[this.viewedName] = true
        this.setMemoryData(this.data)
        this.actionCallback()
    }

    /**
     * Event action accept all cick
     */
    onActionAllClick = () => {
        for (const type in this.data) {
            this.data[type] = true

            if (type != this.viewedName) {
                this.changeScriptType(type, 'js')

                var checkboxElements = document.querySelectorAll('input' + this.getQueryDataBrackets('check', type))

                for (const checkboxElement of checkboxElements) {
                    checkboxElement.checked = 'checked'
                }
            }
        }

        this.setMemoryData(this.data)
        this.actionCallback()
    }
}

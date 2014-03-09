
;(function () {
    "use strict"

    var oucfeed = {
        ajax: function (options) {
            var type = options.type || 'GET'
            var url = options.url
            var data = options.data || ''

            var xhr = new XMLHttpRequest()
            xhr.open(type, url, true)
            if (options.contentType) {
                xhr.setRequestHeader('Content-Type', options.contentType)
            }
            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    var response = xhr.responseText
                    if (options.dataType === 'json') {
                        response = JSON.parse(response)
                    }
                    options.success(response)
                }
            }
            xhr.send(data)
        },
        root: (function () {
            var scripts = document.getElementsByTagName('script')
            var src = scripts[scripts.length-1].src
            var lastSlash = src.lastIndexOf("/")
            var root = lastSlash === -1 ? "" : src.slice(0, lastSlash+1)
            return root
        })(),
        ajaxJSON: function (url, success, data) {
            var options = {
                type: 'GET',
                url: this.root + url,
                success: success,
                dataType: 'json'
            }
            if (data) {
                options.type = 'POST'
                options.data = JSON.stringify(data)
                options.contentType = 'application/json'
            }
            this.ajax(options)
        },
        getCategory: function(callback) {
            this.ajaxJSON('category', callback)
        },
        postProfile: function (profile, callback) {
            this.ajaxJSON("profile", callback, profile)
        },
        getFeedUrl: function(profile_id, feed_type) {
            feed_type = feed_type || 'rss'
            return this.root + feed_type + '/' + profile_id
        }
    }

    window.oucfeed = oucfeed

})()

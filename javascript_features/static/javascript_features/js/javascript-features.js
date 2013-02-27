jQuery(function($) {

    $('body').ajaxComplete(function(event, xhr, options) {
        if(xhr.readyState !== 4) {
            return;
        }

        var featuresJSON = xhr.getResponseHeader("X-JavaScript");
        if(!featuresJSON) {
            return;
        }

        var features = $.parseJSON(featuresJSON);
        for(var i = 0, f; f = features[i]; i++) {
            if(f in window[SITE_NS] && typeof Quail[f].init == "function") {
                var context = $(options.context || "body");
                window[SITE_NS][f].init(context);
            } else if(console && console.warn) {
                console.warn("Unknown JavaScript feature '" + f + "'\n" +
                    "Make sure a "+SITE_NS+"."+f+".init function exists.");
            }
        }
    });

});

import simplejson

class JavaScriptFeaturesMiddleware(object):
    def process_request(self, request):
        request.javascript_features = set()

    def process_response(self, request, response):
        if request.is_ajax() and hasattr(request, "javascript_features") and len(request.javascript_features) > 0:
            features = list(request.javascript_features)
            response['X-JavaScript'] = simplejson.dumps(features)

        return response

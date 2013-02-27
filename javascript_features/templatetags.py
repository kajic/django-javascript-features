"""
Template tags that help us to initialise the correct bits of JavaScript
"""

from django.conf import settings

from jinja2 import contextfunction

@contextfunction
def use_javascript_feature(ctx, request, feature):
    # When the middleware is installed this guard condition shouldn't be
    # needed, but sometimes (e.g. in tests) we don't use the whole stack.
    if hasattr(request, 'javascript_features'):
        request.javascript_features.add(str(feature))
    return ""

@contextfunction
def init_javascript_features(ctx):
    features = ctx["request"].javascript_features
    lines = ["%s.%s.init(context);" % (settings.JAVASCRIPT_FEATURES_NAMESPACE, f) for f in features]
    if len(lines) > 0:
        js = '(function(){ var context = $("body"); %s }());' % " ".join(lines)
        return "<script type='text/javascript'>%s</script>" % js
    else:
        return ""

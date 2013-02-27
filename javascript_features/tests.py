from django.test import TestCase
from django.conf import settings

import simplejson
from django.http import HttpRequest, HttpResponse

from .middleware import JavaScriptFeaturesMiddleware
from .templatetags import init_javascript_features, use_javascript_feature

class JavaScriptFeaturesTest(TestCase):
    def setUp(self):
        self.middleware = JavaScriptFeaturesMiddleware()
        self.request = HttpRequest()
        self.response = HttpResponse()

    def test_normal_request_with_no_features(self):
        self.middleware.process_request(self.request)
        self.middleware.process_response(self.request, self.response)

        self.assertTrue('X-JavaScript' not in self.response)

        script = init_javascript_features(
            {"request": self.request},
        )
        self.assertEqual("", script)

    def test_normal_request_with_features(self):
        self.middleware.process_request(self.request)
        use_javascript_feature(
            self.request,
            "Foo",
        )
        use_javascript_feature(
            self.request,
            "Bar",
        )
        use_javascript_feature(
            self.request,
            "Bar",
        )
        self.middleware.process_response(self.request, self.response)

        self.assertTrue('X-JavaScript' not in self.response)

        script = init_javascript_features(
            {"request": self.request},
        )
        self.assertTrue("%s.Foo.init" % settings.JAVASCRIPT_FEATURES_NAMESPACE in script)
        self.assertTrue("%s.Bar.init" % settings.JAVASCRIPT_FEATURES_NAMESPACE in script)

    def test_ajax_request_with_no_features(self):
        self.request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
        self.assertTrue(
            self.request.is_ajax(),
            "Test setup is wrong, this should be an AJAX request",
        )

        self.middleware.process_request(self.request)
        self.middleware.process_response(self.request, self.response)

        self.assertTrue('X-JavaScript' not in self.response)

    def test_ajax_request_with_features(self):
        self.request.META['HTTP_X_REQUESTED_WITH'] = 'XMLHttpRequest'
        self.assertTrue(
            self.request.is_ajax(),
            "Test setup is wrong, this should be an AJAX request",
        )

        self.middleware.process_request(self.request)
        use_javascript_feature(
            self.request,
            "Foo",
        )
        use_javascript_feature(
            self.request,
            "Bar",
        )
        use_javascript_feature(
            self.request,
            "Bar",
        )
        self.middleware.process_response(self.request, self.response)

        self.assertTrue('X-JavaScript' in self.response)
        header = self.response['X-JavaScript']
        features = simplejson.loads(header)
        self.assertEqual(2, len(features))
        self.assertTrue('Foo' in features and 'Bar' in features)

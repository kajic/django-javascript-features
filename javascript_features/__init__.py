"""
This modules helps us to initialise the right bits of JavaScript on the
right pages and at the right times. It's a port of the javascript-features
Ruby Gem, which can be found at:
    http://github.com/georgebrock/javascript-features/

There are two steps to using this:

1) Write your JavaScript so that each features is contained within an
   object within the project namespace, and that object has an init
   function, e.g. for a feature called Foo:

      project_namespace.Foo = {
          init: function(context) {
              // Set up foo here
          }
      };

2) Indicate in your templates which JavaScript is required, for example
   if you have an element that is enhanced by the project_namespace.Foo
   JavaScript:

      {{ use_javascript_feature(request, "Foo") }}
      <div id='foo'>
        <!-- Markup that is enhanced using Foo's Javascript -->
      </div>

The init function for your JavaScript will be called on any page or after
any AJAX request that renders a template that requests it. The context
passed to the init function will usually be the document's body, but if
you specify a context for your AJAX request (i.e. with
jQuery.ajax({'context': myElement, ...}) ) then that will be passed instead.
"""

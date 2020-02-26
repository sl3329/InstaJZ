from django.views.generic import TemplateView
# HelloWorld is a templateview
class HelloWorld(TemplateView):
    template_name = 'test.html'

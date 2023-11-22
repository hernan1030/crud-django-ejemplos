from django.views.generic import TemplateView

# Create your views here.


class HomePageViews(TemplateView):
    template_name = "core/home.html"

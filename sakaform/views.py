from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

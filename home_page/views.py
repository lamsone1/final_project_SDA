from django.utils import timezone

from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

from utils.models import Box, Fefco


class FrontView(TemplateView):
    template_name = 'front.html'


class AboutView(TemplateView):
    template_name = 'about.html'

class HowToShopView(TemplateView):
    template_name = 'how.html'

class ConditionsView(TemplateView):
    template_name = 'conditions.html'

class CompleteListView(ListView):
    template_name = 'front_full_list.html'
    model = Box

class ProductDetailView(DetailView):
    model = Box
    template_name = 'product_detail.html'


    #queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class FefcoView(ListView):
    template_name = 'fefco_front_list.html'
    model = Fefco

class FrontFefcoListView(ListView):
    template_name = "front_fefco_list.html"
    context_object_name = "fefcolist"

    def get_queryset(self):
        content = {
            'fefcotype': self.kwargs['fefco'],
            'products': Box.objects.filter(fefco__fefco_code=self.kwargs['fefco'])
        }
        return content
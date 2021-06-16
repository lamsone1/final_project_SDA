from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from utils.models import Box

from utils.forms import BoxModelForm, StockModelForm


def boxes(request):
    box_list = Box.objects.all()

    return render(request, template_name='goods_full_list.html', context={'boxes': box_list})


class BoxesListView(ListView):
    template_name = 'goods_list.html'
    model = Box

class BoxUpdateView(UpdateView):
    template_name = 'form.html'
    model = Box
    form_class = BoxModelForm
    success_url = reverse_lazy('utils')

class BoxDeleteView(DeleteView):
    template_name = 'box_confirm_delete.html'
    model = Box
    success_url = reverse_lazy('utils')

class ToStockUpdateView(UpdateView):
    template_name = 'form.html'
    model = Box
    form_class = StockModelForm
    success_url = reverse_lazy('utils')

class BoxCreateView(CreateView):
    template_name = 'form.html'
    form_class = BoxModelForm
    success_url = reverse_lazy('utils')

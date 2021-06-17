from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from utils.models import Box, Fefco

from utils.forms import BoxModelForm, StockModelForm, FefcoModelForm


def boxes(request):
    box_list = Box.objects.all()

    return render(request, template_name='goods_full_list.html', context={'boxes': box_list})


class BoxesListView(LoginRequiredMixin, ListView):
    template_name = 'goods_list.html'
    model = Box

class BoxUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Box
    form_class = BoxModelForm
    success_url = reverse_lazy('utils')

class BoxDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'box_confirm_delete.html'
    model = Box
    success_url = reverse_lazy('utils')

class ToStockUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Box
    form_class = StockModelForm
    success_url = reverse_lazy('utils')

class BoxCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = BoxModelForm
    success_url = reverse_lazy('utils')

class FefcoListView(LoginRequiredMixin, ListView):
    template_name = 'fefco_list.html'
    model = Fefco

class FefcoCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = FefcoModelForm
    success_url = reverse_lazy('utils')

class FefcoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Fefco
    form_class = FefcoModelForm
    success_url = reverse_lazy('utils/fefco')



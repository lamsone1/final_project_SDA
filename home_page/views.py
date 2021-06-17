from django.shortcuts import render
from django.views.generic import ListView

from utils.models import Box


class FrontListView(ListView):
    template_name = 'front.html'
    model = Box

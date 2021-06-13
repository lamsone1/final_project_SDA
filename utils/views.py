from django.shortcuts import render
from django.views.generic import ListView

from utils.models import Box


def boxes(request):
    box_list = Box.objects.all()

    return render(request, template_name='goods_full_list.html', context={'boxes': box_list})


class BoxesListView(ListView):
    template_name = 'goods_full_list.html'
    model = Box

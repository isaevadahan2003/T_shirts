from django.shortcuts import render
from django.views.generic import ListView
from . import models

class T_shitrsView(ListView):
    template_name = 'list/list1.html'
    queryset = models.T_shirts.objects.all()

    def get_queryset(self):
        return models.T_shirts.objects.all()
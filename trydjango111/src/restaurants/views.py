import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    # overrided
    def get_context_data(self, *args, **kwargs):
        # super(HomeView, self) basically gives the TemplateView
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = random.randint(0, 10000000)
        some_list = [num, random.randint(0, 1000000), random.randint(0, 10000000)]
        context.update({
        "bool_item": True,
        "html_var":"context variable",
        "num":num,
        "some_list":some_list
        })
        return context

from django.db.models import Q
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RestaurantLocationCreateForm
from .models import RestaurantLocation


# def restaurant_createview(request):
#     form = RestaurantLocationCreateForm(request.POST or None)
#     errors = None
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/restaurants/")
#     if form.errors:
#         errors = form.errors
#
#     context = {"form":form, "errors":errors}
#     template_name = 'restaurants/form.html'
#     return render(request, template_name, context)

# def restaurant_listview(request):
#     template_name = 'restaurants/restaurants_list.html'
#     query_set = RestaurantLocation.objects.all()
#     context = {
#         "object_list": query_set
#     }
#     return render(request, template_name, context)

class RestaurantListView(ListView):
    def get_queryset(self):
        # slug = self.kwargs.get("slug")
        # if slug:
        #     queryset = RestaurantLocation.objects.filter(
        #         Q(category__iexact=slug) |
        #         Q(category__icontains=slug)
        #     )
        # else:
        queryset = RestaurantLocation.objects.all()
        return queryset

# Note that DetailView will automatically use the object based on
# the slug that was given using the query set
class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

    # #override
    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     # a shortcut to get the object
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)# or pk=rest_id
    #     return obj

class RestaurantCreateView(LoginRequiredMixin, CreateView):
    form_class = RestaurantLocationCreateForm
    #login_url = '/login/' # moved to base.py(settings)
    # because we pretty much want it to redirect to this url
    # for every loginrequired view
    template_name = 'restaurants/form.html'
    #success_url = '/restaurants/'

    #override
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        # form_valid saves after with the super() call
        return super(RestaurantCreateView, self).form_valid(form)

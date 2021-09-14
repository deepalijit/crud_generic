from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Laptop

# Create your views here.

class LaptopListView(ListView):
    model=Laptop
    #template_name=laptop_list.html (is the html which is looked by default by List generic view)
    #we can define it at our own as=>
    #template_name='name of template'

class LaptopCreateView(CreateView):
    model=Laptop
    fields='__all__'
    success_url='/crud/listview'

class LaptopUpdateView(UpdateView):
    model=Laptop
    fields='__all__'
    success_url='/crud/listview'

class LaptopDeleteView(DeleteView):
    model=Laptop
    success_url='/crud/listview'


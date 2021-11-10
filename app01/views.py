from django.shortcuts import render
from .models import *
from django.views.generic import ListView

# Create your views here.
class indexView(ListView):
    model = Mymodel
    template_name = "index.html"

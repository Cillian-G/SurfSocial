from django.shortcuts import render
from django.views import generic
from .models import Beach

class BeachList(generic.ListView):
    model = Beach

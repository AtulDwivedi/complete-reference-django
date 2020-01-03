from django.shortcuts import render
from django.views.generic import ListView
from items.models import Item

class ListItems(ListView):
    model = Item
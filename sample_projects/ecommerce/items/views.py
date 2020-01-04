from django.shortcuts import render
from django.views.generic import ListView, DetailView
from items.models import Item


class ListItems(ListView):
    model = Item


class ItemDetail(DetailView):
    model = Item

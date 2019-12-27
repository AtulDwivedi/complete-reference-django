from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView)
from django.http import HttpResponse
from item.models import (Category, Item)

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'index'
        return context


class ContactUsView(TemplateView):
    template_name = 'contact_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active'] = 'contact_us'
        return context


class AboutUsView(View):
    def get(self, request):
        return HttpResponse('We are perfectionist with deadlines.')

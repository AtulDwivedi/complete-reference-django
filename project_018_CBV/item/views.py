from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from item.models import (Category, Item)
from django.urls import reverse_lazy

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

class CreateCategoryView(CreateView):
    fields = ('name', 'image')
    model = Category

class UpdateCategoryView(UpdateView):
    fields = ('name', 'image')
    model = Category

class DeleteCategoryView(DeleteView):
    model = Category
    success_url = reverse_lazy('item:category_list')

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


class GreetingView(View):
    def get(self, request):
        return HttpResponse('Good morning...!!!')

class AboutUsView(View):
    def get(self, request):
        return render(request, 'about_us.html', {})

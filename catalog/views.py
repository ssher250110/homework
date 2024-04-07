from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.models import Product, Blog


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['description'] = 'Auto parts'
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Page product'
        return context


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'photo', 'category', 'price', ]
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create product'
        return context


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'photo', 'category', 'price', ]
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update product'
        return context


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete product'
        return context


class ContactView(TemplateView):
    template_name = 'catalog/contact_info.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя: {name}, Номер телефона: {phone}, Сообщение: {message}")
        return render(request, self.template_name)


class BlogListView(ListView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog'
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(status=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Page blog'
        return context

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'image', 'status', 'product', ]
    success_url = reverse_lazy('catalog:blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create blog'
        return context


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'image', 'status', 'product', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create blog'
        return context

    def get_success_url(self):
        return reverse('catalog:blog_info', args=[self.object.product.pk])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete blog'
        return context

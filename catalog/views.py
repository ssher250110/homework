from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Blog, Version


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        context['description'] = 'Auto parts'
        for product in context.get('object_list'):
            product.version = product.version_set.filter(is_active_version=True).first()
        return context


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Page product'
        version = self.object.version_set.filter(is_active_version=True).first()
        context['version'] = version
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create product'
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users:login'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_info', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update product'
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context['formset'] = VersionFormset(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']

        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users:login'
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


class BlogCreateView(LoginRequiredMixin, CreateView):
    login_url = 'users:login'
    model = Blog
    fields = ['title', 'image', 'status', 'product', ]
    success_url = reverse_lazy('catalog:blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create blog'
        return context

    def form_valid(self, form):
        if form.is_valid():
            blog = form.save()
            blog.slug = slugify(blog.title)
            blog.save()
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'users:login'
    model = Blog
    fields = ['title', 'image', 'status', 'product', ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update blog'
        return context

    def get_success_url(self):
        return reverse('catalog:blog_info', args=[self.object.product.pk])


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'users:login'
    model = Blog
    success_url = reverse_lazy('catalog:blog')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete blog'
        return context

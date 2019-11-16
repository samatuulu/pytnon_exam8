from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from reporter.models import Product


class IndexView(ListView):
    model = Product
    template_name = 'product/index.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.all()


class ProductView(DetailView):
    model = Product
    template_name = 'product/detail.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/create.html'
    fields = ('name', 'category', 'description', 'photo')

    def get_success_url(self):
        return reverse('reporter:product_detail', kwargs={'pk': self.object.pk})

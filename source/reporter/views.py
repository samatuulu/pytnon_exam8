from django.views.generic import ListView, DetailView

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

from django.urls import path
from .views import IndexView, ProductView, ProductCreateView

app_name = 'reporter'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
]

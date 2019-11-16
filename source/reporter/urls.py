from django.urls import path
from .views import IndexView, ProductView

app_name = 'reporter'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_detail')
]
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'),
    path('create/', views.create_product, name='create'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.product_detail, name='detail'),
]

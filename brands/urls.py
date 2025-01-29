from django.urls import path
from . import views

app_name = 'brands'

urlpatterns = [
    path('create/brand/', views.create_brand, name='brand_create'),
]

from django.urls import path
from . import views

app_name = 'catalogs'

urlpatterns = [
    path('create/category/', views.create_category, name='color_create'),
]

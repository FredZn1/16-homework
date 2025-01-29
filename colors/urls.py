from django.urls import path
from . import views

app_name = 'colors'

urlpatterns = [
    path('create/color/', views.create_color, name='color_create'),
]

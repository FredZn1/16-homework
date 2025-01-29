from django.shortcuts import render, redirect
from .models import Category


def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = Category(name=name, description=description)
        category.save()
        return redirect('home')
    return render(request, 'categories/category_create.html')

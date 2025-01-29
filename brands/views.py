from django.shortcuts import render, redirect
from .models import Brand


def create_brand(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        brand = Brand(name=name, description=description, image=image)
        brand.save()
        return redirect('home')
    return render(request, 'brands/brand-create.html')

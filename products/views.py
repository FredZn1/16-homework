from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from brands.models import Brand
from catalogs.models import Category
from colors.models import Color

def home(request):
    selected_catalogs = None
    products = Product.objects.all()
    catalogs = Category.objects.all()
    category = request.GET.get('category')
    if category:
        products = products.filter(category=category)

    if category:
        products = products.filter(brand__id__in=category)
        selected_catalogs = catalogs.filter(id__in=category)
        catalogs = catalogs.exclude(id__in=category)

    ctx = {
        'products': products,
        'selected_catalogs': selected_catalogs,
        'catalogs':catalogs
    }
    return render(request, 'index.html', ctx)

def product_list(request):
    selected_brands = None
    selected_colors = None
    products = Product.objects.all()
    brands = Brand.objects.all()
    colors = Color.objects.all()
    catalogs = Category.objects.all()
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    brand = [int(x) for x in request.GET.getlist('brand')]
    color = request.GET.getlist('color')
    sort = request.GET.get('sort')

    if min_price:
        products = products.filter(price__gte=float(min_price))
    if max_price:
        products = products.filter(price__lte=float(max_price))

    if brand:
        products = products.filter(brand__id__in=brand)
        selected_brands = brands.filter(id__in=brand)
        brands = brands.exclude(id__in=brand)

    if color:
        products = products.filter(color__id__in=color)
        selected_colors = colors.filter(id__in=color)
        colors = colors.exclude(id__in=color)

    if sort == 'low_to_high':
        products = products.order_by('price')
    elif sort == 'high_to_low':
        products = products.order_by('-price')
    elif sort == 'name_asc':
        products = products.order_by('title')
    elif sort == 'name_desc':
        products = products.order_by('-title')

    ctx = {
        'products': products,
        'brands': brands,
        'catalogs': catalogs,
        'colors': colors,
        'selected_colors': selected_colors,
        'selected_brands': selected_brands
    }
    return render(request, 'products/product-by-category.html', ctx)


def create_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        brand_id = request.POST.get('brand')
        category_id = request.POST.get('category')
        color_id = request.POST.get('color')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        product = Product(
            title=title,
            price=price,
            brand_id=brand_id,
            category_id=category_id,
            color_id=color_id,
            description=description,
            image=image
        )
        product.save()
        return redirect('products:list')
    brands = Brand.objects.all()
    catalogs = Category.objects.all()
    colors = Color.objects.all()
    ctx = {
        'brands': brands,
        'catalogs': catalogs,
        'colors': colors
    }
    return render(request, 'products/product-create.html', ctx)


def product_detail(request, year, month, day, slug):
    product = get_object_or_404(Product, slug=slug, created_at__year=year, created_at__month=month, created_at__day=day)
    ctx = {'product': product}
    return render(request, 'products/product-detail.html', ctx)


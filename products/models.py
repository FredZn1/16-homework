from django.db import models
from django.urls import reverse
from config.utils import BaseModel
from django.utils.text import slugify
from catalogs.models import Category
from brands.models import Brand
from colors.models import Color

class Product(BaseModel):
    title = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='products')
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('products:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def __str__(self):
        return f'{self.title}'

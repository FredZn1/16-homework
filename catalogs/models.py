from django.db import models
from config.utils import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'

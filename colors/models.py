from django.db import models
from config.utils import BaseModel

class Color(BaseModel):
    name = models.CharField(max_length=200)
    hex_code = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'
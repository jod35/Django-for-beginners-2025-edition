from django.db import models

# Create your models here.

"""
class Product:
    id: int primary_key
    name: str
    description: str
    image_url: str
    average_rating: float 2 decimal_places
    created_at datetime
    updated_at datetime
"""


class Product(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()
    image_url = models.ImageField(upload_to="product_imgs/", default="default.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<Product {self.name}>"

    class Meta:
        ordering = ["-created_at"]

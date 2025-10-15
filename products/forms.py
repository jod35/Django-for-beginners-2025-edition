from django import forms
from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image_url"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter the product name"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Enter the product description", "rows": 3}
            ),
            "image_url": forms.FileInput(
                attrs={"class": "form-control"}
            )
        }

from django import forms
from .models import Product

# class ProductCreateForm(forms.Form):
#     name = forms.CharField(max_length=90, required=True,widget=forms.TextInput(
#         attrs={'class': 'form-control mt-2'}
#     ))
#     description = forms.CharField(max_length=5000, widget=forms.Textarea(
#         attrs={'class':'form-control mt-2', 'rows': 3}
#     ))
#     image_url = forms.ImageField(widget=forms.FileInput(
#         attrs={'class':'form-control mt-2'}
#     ))


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image_url"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control mt-2" ,'placeholder':"Enter Product Name"},
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control mt-2", "rows": 3, "placeholder": "Product Description"},
            ),
            "image_url": forms.FileInput(
                attrs={"class": "form-control mt-2"},
            ),
        }

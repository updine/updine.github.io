from django import forms
from .models import Product

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
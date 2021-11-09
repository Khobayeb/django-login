from django import forms
from .models import Category, Subcategory, Product


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control"
    }
    ))
    slug = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control"
    }
    ))

    class Meta:
        model = Category
        fields = "__all__"


class SubcategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control"
    }
    ))
    slug = forms.CharField(widget=forms.TextInput(attrs={
        'class': "form-control"
    }
    ))

    class Meta:
        model = Subcategory
        fields = "__all__"


class ProductForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control"}))
    description = forms.CharField(label="Description", widget=forms.Textarea(
        attrs={'class': "form-control"}))
    price = forms.DecimalField(widget=forms.TextInput(
        attrs={'class': "form-control"}))
    old_price = forms.DecimalField(widget=forms.TextInput(
        attrs={'class': "form-control"}))
    stock = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': "form-control"}))

    slug = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control"}))

    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'title', 'description',
                  'price', 'old_price', 'stock', 'image', 'slug', 'active']

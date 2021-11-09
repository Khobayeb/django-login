from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Subcategory, Product
from .forms import CategoryForm, SubcategoryForm, ProductForm


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def category(request):
    data = Category.objects.all()
    return render(request, 'category_list.html', context={'data': data})


@login_required
def add_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return category(request)

    return render(request, 'add_category.html', context={'form': form})


@login_required
def update_category(request, pk):
    data = Category.objects.get(pk=pk)
    form = CategoryForm(instance=data)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return category(request)

    return render(request, 'update_category.html', context={'form': form})


@login_required
def delete_category(request, pk):
    data = Category.objects.get(pk=pk).delete()
    return category(request)






@login_required
def subcategory(request):
    data = Subcategory.objects.all()
    return render(request, 'subcategory_list.html', context={'data': data})


@login_required
def add_subcategory(request):
    form = SubcategoryForm()
    if request.method == "POST":
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return subcategory(request)

    return render(request, 'add_subcategory.html', context={'form': form})


@login_required
def update_subcategory(request, pk):
    data = Subcategory.objects.get(pk=pk)
    form = SubcategoryForm(instance=data)
    if request.method == 'POST':
        form = SubcategoryForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return subcategory(request)

    return render(request, 'update_subcategory.html', context={'form': form})


@login_required
def delete_subcategory(request, pk):
    data = Subcategory.objects.get(pk=pk).delete()
    return subcategory(request)    





@login_required
def product(request):
    data = Product.objects.all()
    return render(request, 'product_list.html', context={'data': data})


@login_required
def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return product(request)

    return render(request, 'add_product.html', context={'form': form})


@login_required
def update_product(request, pk):
    data = Product.objects.get(pk=pk)
    form = ProductForm(instance=data)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return product(request)

    return render(request, 'update_product.html', context={'form': form})


@login_required
def delete_product(request, pk):
    data = Product.objects.get(pk=pk).delete()
    return product(request)





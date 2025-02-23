from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from backend.forms import CategoryForm, ProductForm
from backend.models import Category, Product


# Create your views here.

def login(request):
    return render(request, 'backend/users/index.html', context={})


def add_category(request):
    tooltip = "Ajout des Catégories"
    context = {
        "tooltip": tooltip,
    }
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES or None)
        context['form'] = form
        if form.is_valid():
            form.save()
            messages.success(request, "Catégorie ajouté avec succès !")
            return redirect('get-all-cat')
        else:
            messages.error(request, f'Formulaire invalide !')
    else:
        form = CategoryForm()
        context['form'] = form
    return render(request, "backend/categories/cat_modal.html", context=context)


def get_cat(request, pk):
    cat = get_object_or_404(Category, pk=pk)

    data = {
        'cat_name': cat.cat_name
    }

    return JsonResponse(data)


def get_categories(request):
    tooltip = "Liste des categories"
    categories = Category.objects.all()
    form = CategoryForm()
    context = {'tooltip': tooltip, 'form': form, 'categories': categories}
    if categories.count() > 0:
        return render(request, 'backend/categories/categories.html', context=context)


def edit_cat(request):
    if request.method == "POST":
        cat_id = request.POST['id']
        cat = get_object_or_404(Category, pk=cat_id)
        form = CategoryForm(request.POST, instance=cat or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Categorie modifie avec succes !")
            return redirect('get-all-cat')
        else:
            messages.error(request,"Formulaire invalide !")
            context = {'form': form, 'cat': cat}
            return render(request, "backend/categories/edit_cat.html", context=context)
    return render(request, "backend/categories/edit_cat.html")


def add_product(request):
    tooltip = "Ajout des produits"
    cat_form = CategoryForm()
    context = {'tooltip': tooltip, 'cat_form': cat_form}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES or None)
        context['form'] = form
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit enregisté avec succès !')
        else:
            messages.error(request, 'Formlaire invalid !')
    else:
        cat_form = CategoryForm()
        form = ProductForm()
        context['cat_form'] = cat_form
        context['form'] = form
    return render(request, 'backend/products/add.html', context=context)


def product_list(request):
    tooltip = "Liste des produits"
    products = Product.objects.all()
    context = {'tooltip': tooltip, 'products': products}
    if products.count() > 0:
        return render(request, 'backend/products/products.html', context=context)
    else:
        return redirect('product-list')


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'backend/products/add.html', {'form': form})

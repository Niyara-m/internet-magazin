from django.shortcuts import render
from . models import Category, Products


def home_page(request):
    all_cat = Category.objects.all()
    all_prod = Products.objects.all()

    context = {'all_products': all_prod,
               'all_categories': all_cat}

    return render(request,'testapp/index.html', context)

def get_all_products(request, pk):
    category = Category.objects.get(id=pk)
    products = Products.objects.filter(category=category)

    context = {'products': products}
    return render(request, 'testapp/all_products.html', context)


from django.shortcuts import render, redirect
from . models import Category, Products, Cart

from . forms import RegistrationForm


def home_page(request):
    all_cat = Category.objects.all()
    all_prod = Products.objects.all()

    context = {'all_products': all_prod,
               'all_categories': all_cat}

    return render(request,'testapp/index.html', context)


def about(request):
    return render(request, 'testapp/about.html')


def contact(request):
    return render(request, 'testapp/contact.html')


def get_all_products(request, pk):
    category = Category.objects.get(id=pk)
    products = Products.objects.filter(category=category)

    context = {'products': products}
    return render(request, 'testapp/all_products.html', context)



def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        context = {'form': form}
    else:
        form = RegistrationForm()
        context = {'form': form}
    return render(request, 'registration/register.html', context)


def add_to_cart(request, product_id):
    if request.method == 'GET':
        #quantity = int(request.POST.get('quantity'))
        prod = Products.objects.get(id=product_id)
        #if quantity <= prod.amount:
        Cart.objects.create(
            user_id=request.user.id,
            product_id=prod,
            #count=quantity
        )
    return redirect('/')

    # quantity = int(request.POST.get('quantity'))
    # prod = Products.objects.get(id=product_id)
    # Cart.objects.create(
    #     user_id=request.user_id,
    #     product_id=prod,
    #     count=quantity
    # )
    # return redirect('/')


def user_cart(request):
    user = request.user.id
    cart = Cart.objects.filter(user_id=user)
    context = {'cart_list': cart}
    return render(request, 'testapp/user_cart.html', context)

def del_item(request, cart_id):
    Cart.objects.get(user_id=request.user.id, id=cart_id).delete()
    return redirect('/my-cart/')

def product_detail(request, product_id):
    product = Products.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'testapp/product.html', context)
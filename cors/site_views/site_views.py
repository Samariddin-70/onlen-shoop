from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from cors.models.products import Category,Cart,Product


def index(request):
    ctg = Category.object.get(id=1)
    products = Product.objects.all()

    try:
        error = request.session.pop('error')
    except:
        error=None

    ctx = {
        'products':products,
        "error":error,

    }
    return render(request, 'site/index.html',ctx )

def account(request):
    ctx = {
    }
    return render(request, 'site/account.html', ctx )


@login_required(login_url='login')
def cart(request, add_id=None):
    if add_id is not None:
        product = Product.objects.filter(id=add_id).first()
        if not product:
            request.session["error"] = "Bunaqa ID li Mahsulot topilmadi"
            return redirect('home')
        cart = Cart.objects.filter(user=request.user, product=product.id).first()
        if cart is not None:
            request.session["error"] = "Bu mahsulot allaqachon savatga qushilgan"
            return redirect('home')
        Cart.objects.create(user=request.user, product=product)
        return redirect("cart")


    carts = Cart.objects.filter(user=request.user)
    ctx = {
        "carts":carts
    }
    return render(request, 'site/cart.html', ctx )

def change_cart(request, cart_id, inc):
    cart = Cart.objects.filter(id=cart_id).first()
    if cart:
        if inc:
            cart.quantity +=1
        else:
            cart.quantity -= 1
        cart.save()
        return JsonResponse({
            'success': 'Muaffaqiyatli!',
            'total_balance':request.user.calculater_cart()
        })
    else:
        return JsonResponse({
            'error':'Cart topilmadi'
        })

def categories(request):
    ctx = {
    }
    return render(request, 'site/categories.html', ctx )

def checkout(request):
    ctx = {
    }
    return render(request, 'site/checkout.html', ctx )
def product_d(request):
    ctx = {
    }
    return render(request, 'site/product_detail.html', ctx )
def products(request):
    ctx = {
    }
    return render(request, 'site/products.html', ctx )

def search(request):
    ctx = {
    }
    return render(request, 'site/search.html', ctx )
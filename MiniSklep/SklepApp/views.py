from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

# Create your views here.
def home_view(request):
<<<<<<< HEAD
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
=======
    return render(request, 'home.html')
>>>>>>> ee5f70b2a57eca1aaa111d23c83862cd244708a5

def item_details(request, product_id):
    product = get_object_or_404(Product, id=product_id, availability=True)
    return render(request, 'item_details.html', {'product': product})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])

    if product_id not in cart:
        cart.append(product_id)

    request.session['cart'] = cart
    return redirect('cart')

def cart(request):
    cart_ids = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart_ids)

    sum = sum(product.price for product in products)

    return render(request, 'cart.html', {
        'products': products,
        'sum': sum
    })
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, CartItem, Order
from django.contrib.auth.decorators import login_required

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(CartItem, user=request.user, product_id=pk)
    item.delete()
    return redirect('cart')


from django.shortcuts import redirect, render
from .models import CartItem

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    if request.method == 'POST':
        for item in cart_items:
            Order.objects.create(
                user=request.user,
                product=item.product,
                quantity=item.quantity
            )
        cart_items.delete()
        return redirect('checkout_success')

    total = sum(item.subtotal() for item in cart_items)
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total': total})


@login_required
def checkout_success(request):
    return render(request, 'checkout_success.html')



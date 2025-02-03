from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Product, Comment, Cart
from app_users.models import Customer


def home_page(request):
    query = request.GET.get('q')
    search = request.GET.get('search', '')

    products = Product.objects.filter(name__icontains=search)

    if query:
        if query == 'expensive':
            products = products.order_by('-new_price')
        elif query == 'cheap':
            products = products.order_by('new_price')
        elif query == 'rating':
            products = products.order_by('-rating')
        elif query == 'new-arrivals':
            products = products.order_by('-created')

    context = {
        'products': products,
        'search': search,
        'is_home_page': True,
        'cart_products_quantity': len(request.user.cart_set.all()) if request.user.is_authenticated else '',
    }

    return render(request, 'index.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        comment = request.POST.get('comment')
        
        if len(comment.strip()) >= 10:
            new_comment = Comment.objects.create(
                owner=request.user,
                product=product,
                body=comment
            )
            new_comment.save()
            return redirect(f'/detail/{product_id}#comments-section')

    context = {
        'product': product,
        'last_3_comments': product.comment_set.all()[::-1][:3]
    }

    return render(request, 'detail.html', context)


@login_required(login_url='login')
def add_to_cart(request, product_id):

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        try:
            cart = Cart.objects.create(
                product=get_object_or_404(Product, id=product_id),
                user=get_object_or_404(Customer, id=request.user.id),
                quantity=quantity
            )
            cart.save()
        except:
            product = request.user.cart_set.all().get(product__id=product_id)
            product.quantity += int(quantity)
            product.save()

    return redirect('detail', product_id=product_id)


@login_required(login_url='login')
def change_cart_product_quantity(request, cart_product_id, action):
    cart_product = get_object_or_404(Cart, id=cart_product_id)
    cart_product.quantity += 1 if action == "increment" else -1
    cart_product.save()
    return redirect('cart')    



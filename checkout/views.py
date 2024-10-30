from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from checkout.templates.forms import OrderForm
from checkout.models import OrderItem


# Create your views here.

def checkout(request):
    cart = request.session.get('cart', {})
    total_cart_price = sum(item['total_price'] for item in cart.values())
    form = OrderForm()

    context = {
        'cart': cart,
        'total_cart_price': total_cart_price,
        'form': form,
    }
    return render(request, 'checkout.html', context)


def order_create(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            if form.cleaned_data.get('password'):
                email = form.cleaned_data['email']

                user = User.objects.create_user(username=email, password=form.cleaned_data['password'], email=email)
                user.save()

                login(request, user)

            for item_id, item_data in cart.items():
                OrderItem.objects.create(
                    order=order,
                    product_name=item_data['name'],
                    quantity=item_data['quantity'],
                    price=item_data['price'],
                )
            request.session['cart'] = {}
            request.session.modified = True

            return redirect('order_confirmation')
    else:
        form = OrderForm()

    return render(request, 'checkout.html', {'form': form, 'cart': cart})

def order_confirmation(request):
    return render(request, 'order_confirmation.html')
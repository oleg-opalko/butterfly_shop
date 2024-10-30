import json

from django.http import JsonResponse
from django.shortcuts import render

from shop.models import Product


# Create your views here.

def cart(request):

    current_cart = request.session.get('cart', {})

    for product_id, product_data in current_cart.items():
        product_data['total_price'] = product_data['price'] * product_data['quantity']

    context = {
        'cart': current_cart,
    }

    return render(request, 'cart.html', context)


from django.http import JsonResponse
import json

def add_to_cart(request):
    if request.method == 'POST':
        try:
            product_id = str(request.GET.get('productId'))
            quantity = int(request.GET.get('quantity'))
            size = request.GET.get('size')

            if not product_id or quantity <= 0:
                return JsonResponse({'error': 'Invalid product ID or quantity'}, status=400)

            if size is None:
                return JsonResponse({'message': 'Size is required! \n Please select size in Shop Detail'}, status=200)

            current_cart = request.session.get('cart', {})

            try:
                product = Product.objects.get(pk=product_id)
            except Product.DoesNotExist:
                return JsonResponse({'error': 'Product does not exist'}, status=404)

            product_key = f'{product_id}_{size}'

            if product_key in current_cart:
                current_cart[product_key]['quantity'] += quantity
            else:
                current_cart[product_key] = {
                    'name': product.name,
                    'price': float(product.price),
                    'image': product.main_image.url,
                    'quantity': quantity,
                    'size': size,
                    'total_price': float(product.price) * quantity
                }

            request.session['cart'] = current_cart

            total_quantity = sum(item['quantity'] for item in current_cart.values())
            total_price = sum(item['price'] * item['quantity'] for item in current_cart.values())

            return JsonResponse({
                'message': 'Product added to cart',
                'total_quantity': total_quantity,
                'total_price': f'${total_price}'
            })
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except ValueError:
            return JsonResponse({'error': 'Invalid quantity'}, status=400)
        except Exception as e:
            print(f'Unexpected error: {e}')
            return JsonResponse({'error': 'An unexpected error occurred'}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)

def update_cart_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = str(data.get('product_id'))
            new_quantity = int(data.get('quantity'))

            current_cart = request.session.get('cart', {})

            if product_id in current_cart:
                current_cart[product_id]['quantity'] = new_quantity
                total_price = current_cart[product_id]['price'] * new_quantity

                for item in current_cart.values():
                    item['total_price'] = item['price'] * item['quantity']

                total_quantity = sum(item['quantity'] for item in current_cart.values())
                total_cart_price = sum(item['price'] * item['quantity'] for item in current_cart.values())

                request.session['cart'] = current_cart

                return JsonResponse({
                    'success': True,
                    'total_price': total_price,
                    'total_quantity': total_quantity,
                    'total_cart_price': total_cart_price
                })
            else:
                return JsonResponse({'success': False, 'error': 'Item not found in cart'}, status=404)

        except (json.JSONDecodeError, ValueError):
            return JsonResponse({'success': False, 'error': 'Invalid data'}, status=400)

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


def remove_cart_item(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = str(data.get('product_id'))

            current_cart = request.session.get('cart', {})

            if product_id in current_cart:
                del current_cart[product_id]

                request.session['cart'] = current_cart

                total_quantity = sum(item['quantity'] for item in current_cart.values())
                total_cart_price = sum(item['price'] * item['quantity'] for item in current_cart.values())

                return JsonResponse({
                    'success': True,
                    'total_quantity': total_quantity,
                    'total_cart_price': total_cart_price
                })
            else:
                return JsonResponse({'success': False, 'error': 'Item not found in cart'}, status=404)

        except (json.JSONDecodeError, ValueError):
            return JsonResponse({'success': False, 'error': 'Invalid data'}, status=400)

    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)




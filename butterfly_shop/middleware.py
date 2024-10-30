class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_cart = request.session.get('cart', {})

        self.update_cart_totals(current_cart)

        total_quantity = sum(item['quantity'] for item in current_cart.values())
        total_price = sum(item['total_price'] for item in current_cart.values())

        request.cart_total_quantity = total_quantity
        request.cart_total_price = total_price

        response = self.get_response(request)
        return response

    def update_cart_totals(self, cart):
        for item in cart.values():
            item['total_price'] = item['price'] * item['quantity']

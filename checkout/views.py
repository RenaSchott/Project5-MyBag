from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shoppingcart = request.session.get('shoppingcart ', {})
    if not shoppingcart:
        messages.error(request, "There's nothing in your shoppingcart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Pf038G2ntbCuy5Rl6DUaWdzkb9oD1L28hmfz0JPgrnv3deWweAPnIYTF3XFE6aCecqIeNensbuNkc7vcQjCvNcU00DBtwxTaX',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from products.models import Product


def view_shoppingcart(request):
    """ A view that renders the shopping cart """

    return render(request, 'shoppingcart/shoppingcart.html')


def add_to_shoppingcart(request, item_id):

    """ Add a quantity of the specified product to the shoppingcart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingcart = request.session.get('shoppingcart', {})

    if item_id in list(shoppingcart.keys()):
        shoppingcart[item_id] += quantity
        messages.success(request,
                         f'New: {product.name} qty: {shoppingcart[item_id]}.')
    else:
        shoppingcart[item_id] = quantity
        messages.success(request,
                         f'Added {product.name} to your shoppingcart.')

    request.session['shoppingcart'] = shoppingcart
    return redirect(redirect_url)


def adjust_shoppingcart(request, item_id):
    """Adjust the quantity of the specified product in the shoppingcart"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shoppingcart = request.session.get('shoppingcart', {})

    if quantity > 0:
        shoppingcart[item_id] = quantity
        messages.success(request,
                         f'New: {product.name} qty: {shoppingcart[item_id]}.')
    else:
        shoppingcart.pop(item_id)
        messages.success(request, f'Removed {product.name} from shoppingcart.')

    request.session['shoppingcart'] = shoppingcart
    return redirect(reverse('view_shoppingcart'))


def remove_from_shoppingcart(request, item_id):
    """Remove the specified product in the shoppingcart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        shoppingcart = request.session.get('shoppingcart', {})

        shoppingcart.pop(item_id)
        messages.success(request, f'Removed {product.name} from shoppingcart.')

        request.session['shoppingcart'] = shoppingcart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

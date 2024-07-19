from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from products.models import Product

# Create your views here.

def view_shoppingcart(request):
    """ A view that renders the shopping cart """

    return render(request, 'shoppingcart/shoppingcart.html')


def add_to_shoppingcart(request, item_id):
    """ Add a quantity of the specified product to the shoppingcart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shoppingcart = request.session.get('shoppingcart', {})

    if item_id in list(shoppingcart.keys()):
        shoppingcart[item_id] += quantity
    else:
        shoppingcart[item_id] = quantity

    request.session['shoppingcart'] = shoppingcart
    return redirect(redirect_url)


def adjust_shoppingcart(request, item_id):
    """Adjust the quantity of the specified product in the shoppingcart"""

    quantity = int(request.POST.get('quantity'))
    shoppingcart = request.session.get('shoppingcart', {})

    if quantity > 0:
        shoppingcart[item_id] = quantity

    else:
        shoppingcart.pop(item_id)

    request.session['shoppingcart'] = shoppingcart
    return redirect(reverse('view_shoppingcart'))


def remove_from_shoppingcart(request, item_id):
    """Remove the specified product in the shoppingcart"""

    try:
        shoppingcart = request.session.get('shoppingcart', {})

        shoppingcart.pop(item_id)

        request.session['shoppingcart'] = shoppingcart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

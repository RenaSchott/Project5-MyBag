from django.shortcuts import render, redirect

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

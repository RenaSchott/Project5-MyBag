from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_shoppingcart(request):
    """ A view that renders the shopping cart """

    return render(request, 'shoppingcart/shoppingcart.html')

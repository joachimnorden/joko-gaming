from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.models import Product
from profiles.models import UserProfile
from .models import Wishlist


@login_required
def wishlist(request):
    """ wishlist page """

    template = 'wishlist/wishlist.html'
    context = {
        'on_page': True,
    }
    return render(request, template, context)

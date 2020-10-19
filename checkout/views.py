from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    photobag = request.session.get('photobag', {})
    if not photobag:
        messages.error(request, "There's nothing in your photobag at the moment")
        return redirect(reverse('photos'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HdwkSG2rykvupn8Uj5STNDuKlk8FNHQCO964jyzGKUj14GGEfMHkJ8LSEJBLV4aoYQydW9Oeba2dLfvY0jM6FZs002m4A2Pdz',
        'client_secret': 'some test key for client secret',
    }

    return render(request, template, context)
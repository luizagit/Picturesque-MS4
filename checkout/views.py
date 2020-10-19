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
    }

    return render(request, template, context)
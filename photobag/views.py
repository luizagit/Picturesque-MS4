from django.shortcuts import render, redirect

# Create your views here.

def view_photobag(request):
    """ A view that renders the bag contents page """

    return render(request, 'photobag/photobag.html')


def add_to_photobag(request, item_id):
    """ Add a quantity of the specified product to the photoshopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    photobag = request.session.get('photobag', {})

    if item_id in list(photobag.keys()):
        photobag[item_id] += quantity
    else:
        photobag[item_id] = quantity

    request.session['photobag'] = photobag
    return redirect(redirect_url)
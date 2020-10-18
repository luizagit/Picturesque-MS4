from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from photos.models import Photo

# Create your views here.

def view_photobag(request):
    """ A view that renders the bag contents page """

    return render(request, 'photobag/photobag.html')


def add_to_photobag(request, item_id):
    """ Add a quantity of the specified photo to the photoshopping bag """

    photo = get_object_or_404(Photo, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    photobag = request.session.get('photobag', {})

    if item_id in list(photobag.keys()):
        photobag[item_id] += quantity
        messages.success(request, f'Updated {photo.name} quantity to {photobag[item_id]}')
    else:
        photobag[item_id] = quantity
        messages.success(request, f'Added {photo.name} to your photobag')

    request.session['photobag'] = photobag
    return redirect(redirect_url)

def adjust_photobag(request, item_id):
    """Adjust the quantity of the specified photo to the specified amount"""

    photo = get_object_or_404(Photo, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    photobag = request.session.get('photobag', {})

    if quantity > 0:
        photobag[item_id] = quantity
        messages.success(request, f'Updated {photo.name} quantity to {photobag[item_id]}')

    else:
        photobag.pop(item_id)
        messages.success(request, f'Removed {photo.name} from your photobag')

    request.session['photobag'] = photobag
    return redirect(reverse('view_photobag'))

def remove_photo_from_bag(request, item_id):
    """Remove the photo from the PhotoShopping bag"""

    try:
        photo = get_object_or_404(Photo, pk=item_id)
        photobag = request.session.get('photobag', {})

        photobag.pop(item_id)
        messages.success(request, f'Removed {photo.name} from your bag')

        request.session['photobag'] = photobag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from photos.models import Photo

def photobag_contents(request):

    photobag_items = []
    total = 0
    photo_count = 0

    photobag = request.session.get('photobag', {})

    for item_id, quantity in photobag.items():
        photo = get_object_or_404(Photo, pk=item_id)
        total += quantity * photo.price
        photo_count += quantity
        photobag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'photo': photo,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total
    
    context = {
        'photobag_items': photobag_items,
        'total': total,
        'photo_count': photo_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

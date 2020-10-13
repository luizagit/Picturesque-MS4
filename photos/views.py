from django.shortcuts import render, get_object_or_404
from .models import Photo

# Create your views here.

def all_photos(request):
    """ A view to show all photos, with sorting feature included"""

    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'photos/photos.html', context)

    
def photo_detail(request, photo_id):
    """ A view to show individual photo characteristics """

    photo = get_object_or_404(Photo, pk=photo_id)

    context = {
        'photo': photo,
    }

    return render(request, 'photos/photo_detail.html', context)
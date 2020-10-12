from django.shortcuts import render
from .models import Photo

# Create your views here.

def all_photos(request):
    """ A view to show all photos, with sorting feature included"""

    photos = Photo.objects.all()

    context = {
        'photos': photos,
    }

    return render(request, 'photos/photos.html', context)
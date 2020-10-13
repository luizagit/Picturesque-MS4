from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Category

# Create your views here.

def all_photos(request):
    """ A view to show all photos, with sorting feature included"""

    photos = Photo.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            photos = photos.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


    context = {
        'photos': photos,
        'existent_categories': categories,
    }

    return render(request, 'photos/photos.html', context)

    
def photo_detail(request, photo_id):
    """ A view to show individual photo characteristics """

    photo = get_object_or_404(Photo, pk=photo_id)

    context = {
        'photo': photo,
    }

    return render(request, 'photos/photo_detail.html', context)
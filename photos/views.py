from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models.functions import Lower
from .models import Photo, Category
from .forms import PhotoForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def all_photos(request):
    """ A view to show all photos, with sorting feature included"""

    photos = Photo.objects.all()
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                photos = photos.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey == 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
        
            photos = photos.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            photos = photos.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    existent_sorting = f'{sort}_{direction}'

    context = {
        'photos': photos,
        'existent_categories': categories,
        'existent_sorting': existent_sorting,
    }

    return render(request, 'photos/photos.html', context)

    
def photo_detail(request, photo_id):
    """ A view to show individual photo characteristics """

    photo = get_object_or_404(Photo, pk=photo_id)

    context = {
        'photo': photo,
    }

    return render(request, 'photos/photo_detail.html', context)


@login_required
def add_photo(request):
    """ Add a photo to the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you need to be a Picturesque admin to perform this operation.'
            )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()
            messages.success(request, 'Photo successfully added!')
            return redirect(reverse('photo_detail', args=[photo.id]))
        else:
            messages.error(request, 'Failed to add photo. Please ensure the form is valid.')
    else:
        form = PhotoForm()

    template = 'photos/add_photo.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_photo(request, photo_id):
    """ Edit a photo in the store """
    if not request.user.is_superuser:
        messages.error(request, 
        'Sorry, you need to be a Picturesque admin to perform this operation.'
        )
        return redirect(reverse('home'))

    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Photo successfully updated!')
            return redirect(reverse('photo_detail', args=[photo.id]))
        else:
            messages.error(request, 'Failed to update photo. Please ensure the form is valid.')
    else:
        form = PhotoForm(instance=photo)
        messages.info(request, f'You are editing {photo.name}')

    template = 'photos/edit_photo.html'
    context = {
        'form': form,
        'photo': photo,
    }

    return render(request, template, context)

@login_required
def delete_photo(request, photo_id):
    """ Delete a photo from the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, you need to be a Picturesque admin to perform this operation.'
            )
        return redirect(reverse('home'))

    photo = get_object_or_404(Photo, pk=photo_id)
    photo.delete()
    messages.success(request, 'Photo deleted!')
    return redirect(reverse('photos'))

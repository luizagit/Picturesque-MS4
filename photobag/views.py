from django.shortcuts import render

# Create your views here.

def view_photobag(request):
    """ A view that renders the bag contents page """

    return render(request, 'photobag/photobag.html')
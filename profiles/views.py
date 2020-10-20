from django.shortcuts import render

# Create your views here.

def user_profile(request):
    """ Display user profile. """

    template = 'profiles/user_profile.html'
    context = {}

    return render(request, template, context)
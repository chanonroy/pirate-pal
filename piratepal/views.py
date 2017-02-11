from django.shortcuts import render

def landing(request):
    """ Landing page """
    return render(request, 'landing/index.html', context=None)

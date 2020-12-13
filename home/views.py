from django.shortcuts import render, HttpResponse


def home_view(request):
    if request.user.is_authenticated():
        context = {
            'isim': request.user.username
        }
    else:
        context = {
            'isim': 'Misafir'
        }
    return render(request, 'home.html', context)


def aboutme_view(request):
    if request.user.is_authenticated():
        context = {
            'isim': request.user.username
        }
    else:
        context = {
            'isim': 'Misafir'
        }
    return render(request, 'aboutme.html', context)


def contactme_view(request):
    if request.user.is_authenticated():
        context = {
            'isim': request.user.username
        }
    else:
        context = {
            'isim': 'Misafir'
        }
    return render(request, 'contactme.html', context)
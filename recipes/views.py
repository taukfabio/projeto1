# from django.shortcuts import render
from django.http import HttpResponse
# from django.urls import path
from django.shortcuts import render


# Create your views here.
def home(request):

    # return HttpResponse('Home! 2')
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Fabio Tauk'
    })


def recipe(request, id):

    # return HttpResponse('Home! 2')
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Fabio Tauk'
    })


def contato(request):

    return render(request, 'recipes/pages/contato.html')


def quiz_flutter(request):

    return render(request, 'quiz/index.html')


def sobre(request):

    return HttpResponse('Sobre!')

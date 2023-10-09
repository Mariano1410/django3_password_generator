from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charactersupper = list('ABCDEFGHIJKLMNOPRSTUV')
        characters.extend(charactersupper)
    
    if request.GET.get('special'):
        charactersspecial = list('!"#$%&/()=?¡¨*[]_:;,.-°|¬´~`^ñ+}{')
        characters.extend(charactersspecial)
    
    if request.GET.get('numbers'):
        charactersnumber = list('1234567890')
        characters.extend(charactersnumber)

    length = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
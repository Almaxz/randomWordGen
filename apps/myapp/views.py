from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    request.session.clear()
    if "counter" not in request.session:
        request.session['counter'] = 0
    return render(request,"index.html") 

def random_word(request):
    if "counter" not in request.session:
        request.session['counter'] = 1
    else: 
        request.session['counter'] += 1
    context = {
        "random_word": get_random_string(length = 14)
    }
    return render(request, "index.html", context)
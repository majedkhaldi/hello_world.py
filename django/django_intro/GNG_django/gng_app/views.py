from django.shortcuts import render, redirect
import random

def index(request):
    if 'random' not in request.session:
        request.session['random']= random.randint(1,100)
    if 'counter' not in request.session:
        request.session['counter'] = 0
        request.session['counter'] = 0
    return render(request,"index.html")

def number(request):
    request.session['counter']+=1
    guessed_number=int(request.POST['random_number'])
    if guessed_number > request.session['random']:
        request.session['message'] = 'Too high!'
    elif guessed_number < request.session['random']:
        request.session['message'] = 'Too low!'
    elif guessed_number == request.session['random']:
        request.session['message']='Win'
    return redirect ('/')

def clear(request):
    del request.session['counter']
    del request.session['random']
    del request.session['message']
    return redirect('/')
# Create your views here.

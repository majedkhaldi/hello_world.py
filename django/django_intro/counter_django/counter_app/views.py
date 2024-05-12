from django.shortcuts import render, redirect

def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    return render (request, "index.html")

def inrementbytwo(request):
    request.session['counter'] += 1
    if 'counter2' in request.session:
        request.session['counter2'] += 2
    else:
        request.session['counter2'] = 2
    return redirect("/")

def reset(request):
    del request.session['counter']
    if 'counter2' in request.session:
        del request.session['counter2']
    return redirect("/")

def incbyuser(request):
    number = int(request.POST['userinput'])
    request.session['counter'] += number-1
    request.session['counter2'] += number
    return redirect ("/")


# Create your views here.

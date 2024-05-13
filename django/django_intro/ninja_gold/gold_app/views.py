from django.shortcuts import render, redirect
import random
from time import gmtime, strftime
def index(request):
    if 'message' not in request.session:
        request.session['message'] = ''
    if 'golds' not in request.session:
        request.session['golds'] = 0
    return render(request,"index.html")

def addgold(request,place):
    findgold = int(random.randint(10,20))
    request.session['golds'] += findgold
    # place = request.POST['place']
    timess = strftime("%Y-%m-%d %H:%M %p", gmtime())
    # request.session['message'] += 'You entered a '+ place + " and you earned " + str(request.session['findgold']) + " coins! HURRAY!!"
    request.session['message'] = '<li class="green"> You entered a '+ place + " and you earned " + str(findgold) + " coins! HURRAY!! " + timess + ' </li>' + request.session['message']
    return redirect('/')

def addorlosegold(request,place):
    findgold = int(random.randint(-50,50))
    request.session['golds'] += findgold
    # place = request.POST['place']
    timess = strftime("%Y-%m-%d %H:%M %p", gmtime())
    if findgold >= 0:
        request.session['message'] = '<li class="green"> You won a '+ place + " and you earned " + str(findgold) + " coins! HURRAY!! " + timess + ' </li>' + request.session['message']
    else:
        request.session['message'] = '<li class="red"> You failed a '+ place + " and you lost " + str(findgold*-1) + " coins! OUCH!! " + timess + ' </li>' + request.session['message']
    return redirect('/')

def deleteall(request):
    request.session.flush()
    return redirect ('/')

# Create your views here.

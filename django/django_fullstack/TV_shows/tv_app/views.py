from django.shortcuts import render, redirect
from .models import Tvshow

def index(request):
    data = {
        "shows": Tvshow.objects.all()
    }
    return render(request, "shows.html", data)

def addnew_form(request):
    return render(request, "addnew.html")

def addnew(request):
    title = request.POST['title']
    network = request.POST['network']
    releasedate = request.POST['releasedate']
    descritopn = request.POST['description']
    Tvshow.objects.create(title = title, network = network, release_date = releasedate, description = descritopn)
    return redirect('/shows/new')

def delete(request, x):
    todelete = Tvshow.objects.get(id = x)
    todelete.delete()
    return redirect('/shows')

def showtheshow(request,x):
    showobject = Tvshow.objects.get(id = x)
    data = {
        "id" : showobject.id,
        "title" : showobject.title,
        "network" : showobject.network,
        "description" : showobject.description,
        "releasedate" : showobject.release_date,
        "update" : showobject.updated_at
    }
    return render(request, "showinfo.html", data)
# Create your views here.

def editpage(request,x):

    showobject = Tvshow.objects.get(id = x)
    data = {
        "id": showobject.id,
        "title" : showobject.title,
        "network" : showobject.network,
        "description" : showobject.description,
        "releasedate" : showobject.release_date.strftime('%Y-%m-%d'),
    }
    return render(request, "editing.html", data)

def editshow(request,x):
    showobject = Tvshow.objects.get(id = x)

    utitle = request.POST['title']
    unetwork = request.POST['network']
    ureleasedate = request.POST['releasedate']
    udescritopn = request.POST['description']
    
    showobject.title = utitle
    showobject.network = unetwork
    showobject.release_date = ureleasedate
    showobject.description = udescritopn

    showobject.save()
    return redirect('/shows')
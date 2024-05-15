from django.shortcuts import render,redirect
from .models import Dojo, Ninja
# Create your views here.
def index(request):
     data = {
          "dojos": Dojo.objects.all(),
          "ninjas": Ninja.objects.all(),
     }
     return render(request,"index.html", data)

def inputdojos(request):
     name = request.POST['name']
     city = request.POST['city']
     state = request.POST['state']
     Dojo.objects.create(name = name, city = city, state = state)
     return redirect("/")

def inputninjas(request):
     fname = request.POST['fname']
     lname = request.POST['lname']
     dojo = request.POST['dojo']
     dojoinninja = Dojo.objects.get(name = dojo)
     Ninja.objects.create(first_name = fname, last_name = lname, dojo = dojoinninja)
     return redirect("/")

def deleted(request,x):
     tobedeleted = Dojo.objects.get(id=x)
     tobedeleted.delete()
     return redirect("/")
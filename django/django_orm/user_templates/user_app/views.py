from django.shortcuts import render, redirect
from .models import User
def index(request):
    data = {
        "i" : User.objects.all()
    }
    return render(request,"index.html",data)

def adduser(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    age = int(request.POST['age'])
    User.objects.create(first_name=fname, last_name=lname, email_address=email, age=age)
    return redirect("/")
    
# Create your views here.

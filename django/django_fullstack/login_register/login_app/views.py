from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    if 'userid' in request.session:
        del request.session['userid']
    return render(request,"index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            if key == 'email':
                messages.error(request, value, extra_tags= 'email')
            if key == 'fname':
                messages.error(request, value, extra_tags= 'fname')
        return redirect('/')
    else:
        request.session['fname'] = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create(first_name = request.session['fname'], last_name = lname, email = email, password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())
        return redirect('/success')

def login(request):
    user = User.objects.filter(email = request.POST['loginemail'])
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['loginpassword'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
    else:
        messages.error(request,'this email cannot be found', extra_tags= 'emailnotfound')
        return redirect('/')
        
def success(request):
    if 'userid' not in request.session:
        return redirect('/')
    return render(request,"success.html")

def logout(request):
    del request.session['userid']
    return redirect ('/')



# Create your views here.

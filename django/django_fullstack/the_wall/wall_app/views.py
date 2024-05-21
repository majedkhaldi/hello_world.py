from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message,Comment
import bcrypt

def index(request):
    if 'userid' in request.session:
        return redirect('/wall')

    return render(request,"index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags= 'registration')
        return redirect('/')
    else:
        request.session['fname'] = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create(first_name = request.session['fname'], last_name = lname, email = email, password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode())
        return redirect('/wall')

def login(request):
    user = User.objects.filter(email = request.POST['loginemail'])
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['loginpassword'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/wall')
    else:
        messages.error(request,'this email cannot be found', extra_tags= 'emailnotfound')
        return redirect('/')
        
def wall(request):
    if 'userid' not in request.session:
        return redirect('/')
    data = {
    "messages": Message.objects.all()
    }
    return render(request,"success.html", data)

def logout(request):
    del request.session['userid']
    return redirect ('/')

def createpost(request,x):
    message = request.POST['message']
    Message.objects.create(text = message, users = User.objects.get(id=x))
    return redirect('/wall')

def addcomment(request,x,y):
    comment = request.POST['aa']
    Comment.objects.create(text = comment, messages = Message.objects.get(id = x), users = User.objects.get(id = y))
    return redirect('/wall')

def deletecomment(request,x,y):
    comment1 = Comment.objects.get(id = x)
    print(comment1.time)
    if y == int(comment1.users.id):
        comment1.delete()
    # else:
    #     pass
    return redirect('/wall')

# Create your views here.


# Create your views here.

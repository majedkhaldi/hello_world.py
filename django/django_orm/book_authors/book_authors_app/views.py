from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    data = {
        "bk" : Book.objects.all(),
        "au" : Author.objects.all()
    }
    return render(request, "index.html",data)

def auth(request):
    data = {
        "bk" : Book.objects.all(),
        "au" : Author.objects.all()
    }
    return render(request, "author.html",data)

def addbook(request):

    title = request.POST['title']
    desc = request.POST['desc']
    Book.objects.create(title = title, desc = desc)
    return redirect("/")

def addauthor(request):

    fname = request.POST['fname']
    lname = request.POST['lname']
    notes = request.POST['notes']
    Author.objects.create(first_name = fname, last_name = lname, notes = notes)
    return redirect("/authors")

def bookview(request,x):

    this_book = Book.objects.get(id=x)
    # if request.method == 'GET':

    data = {
    "title" : this_book.title,
    "id" : this_book.id,
    "desc" : this_book.desc,
    "au" : this_book.Authors.all(),
    "extraauthors": Author.objects.all(),
    }
    
    if request.method == 'POST':
        newauthor = Author.objects.get(id = request.POST['authorinbook'])
        this_book.Authors.add(newauthor)
  
    return render(request, "book.html", data)


def authorview(request,x):

    this_author = Author.objects.get(id=x)
    # if request.method == 'GET':

    data = {
    "fname" : this_author.first_name,
    "lname" : this_author.last_name,
    "id" : this_author.id,
    "notes" : this_author.notes,
    "bk" : this_author.books.all(),
    "extrabook": Book.objects.all(),
    }
    
    if request.method == 'POST':
        newbook = Book.objects.get(id = request.POST['booktoauthor'])
        this_author.books.add(newbook)
  
    return render(request, "authorinfo.html", data)
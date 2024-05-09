from django.shortcuts import render, redirect
from time import gmtime, strftime
def index(request):
    context = {
        "time": strftime("%H:%M %p", gmtime()),
        "date": strftime("%Y-%m-%d", gmtime()),}
    return render (request, "index.html", context)


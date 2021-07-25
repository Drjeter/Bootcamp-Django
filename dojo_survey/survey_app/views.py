from os import name
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')

def submission(request):
    if request.method == "POST":
        name = request.POST["name"]
        location = request.POST["location"]
        language = request.POST["language"]
        comment = request.POST["comment"]
        redirect(result)

# def back_home(request):

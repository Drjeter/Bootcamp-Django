from os import name
from django.shortcuts import render, redirect

languages = (
    'Python', 'JavaScript'
)
locations = (
    'San Jose', 'Online'
)

def home(request):
    context = {
        'languages': languages,
        'locations': locations,
    }
    return render(request, 'home.html', context)

def submission(request):
    if request.method == "GET":
        return redirect('/')
    request.session['result'] = {
        'name': request.POST['name'],
        'location': request.POST['location'],
        'language': request.POST['language'],
        'comment': request.POST['comment'],
    }
    return redirect('/result')

def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)
    
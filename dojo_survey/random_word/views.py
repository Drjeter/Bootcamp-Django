from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string 

# Create your views here.
def random_word(request):
    if 'random_word' not in request.session:
        request.session['random_word'] = {'attempt' : 0}
    request.session['random_word'] = {
        'word': get_random_string(length=14),
        'attempt': request.session['random_word']['attempt'] + 1
    }
    context = {
        'random_word': request.session['random_word']
    }
    return render(request, 'random_word.html', context)

def reset(request):
    request.session.flush()
    return redirect('/random_word')

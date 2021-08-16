from .models import User
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
    	"all_users": User.objects.all()
    }
    return render(request, "index.html", context)

# show all of the data from a table
def add(request):
    if request.method == 'POST':
        new_user = User.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email_address=request.POST.get("email"),
            age=int(request.POST.get("age")),
            )
        new_user.save()
    return redirect("/")


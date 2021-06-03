from django.shortcuts import render, redirect

from .models import Users


def index(request):
    context = {
        "users": Users.objects.all() # gives me a list
    }
    return render(request, 'index.html', context)


def create_user(request):
    print(request.POST)

    Users.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email_address'],
        age = request.POST['age']
    )
    return redirect("/")
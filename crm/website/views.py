from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
        else:
            messages.success(
                request, "There was an error logging in, please try again."
            )
    return render(request, "home.html")

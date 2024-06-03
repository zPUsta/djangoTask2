from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def register__view(request):
    form = RegisterForm(request.POST or None)  
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        newUser = User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        return redirect("home")
  
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login__view(request):
     form = LoginForm(request.POST or None)  
     if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            return render(request, "login.html")
        login(request, user)
        return redirect("home")

     context = {
        "form": form,
    }
     return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("home")
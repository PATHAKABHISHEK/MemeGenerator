from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def homepage(request):
    return render(request=request, template_name='memeapp/homepage.html',
           context={})

def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("memeapp:homepage")


    form = AuthenticationForm()
    return render(request=request, template_name='memeapp/loginpage.html',
                  context={'form': form})

def registerpage(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = form.save()
            login(request, user)
            return redirect("memeapp:homepage")

    form = RegistrationForm()
    return render(request=request, template_name='memeapp/registerpage.html',
                  context={'form': form})


def logoutpage(request):
    logout(request)
    return redirect("memeapp:homepage")

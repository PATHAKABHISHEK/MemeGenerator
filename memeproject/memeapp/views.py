from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request=request, template_name='memeapp/homepage.html',
           context={})

def loginpage(request):
    return render(request=request, template_name='memeapp/loginpage.html',
                  context={})

def registerpage(request):
    return render(request=request, template_name='memeapp/registerpage.html',
                  context={})

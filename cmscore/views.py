from django.shortcuts import render, redirect


def index(request):
    return render(request, "login.html",{})

def redirect_to_login(request):
    return redirect('login')
 

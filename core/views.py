from django.shortcuts import render
from core.partners import UserManager

def home(request):
    user_manager = UserManager()
    users = user_manager.fetch_all_partners()
    return render(request,"home.html", {"users":users})

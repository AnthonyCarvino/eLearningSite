from django.shortcuts import render

def welcomeHome(request):
    return render(request, 'home.html')
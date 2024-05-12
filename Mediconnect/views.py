from django.shortcuts import render

def home(request):
    # Render the home page template
    return render(request, 'home.html')
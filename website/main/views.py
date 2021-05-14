from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def table(request):
    return render(request, 'main/table.html')

def button(request):
    return render(request, 'main/button.html')
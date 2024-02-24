from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def images(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def collection(request):
    return render(request, 'collection.html')

def assignment(request):
    return render(request, 'assignment.html')
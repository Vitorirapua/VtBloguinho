from django.shortcuts import render

def index(request):
    return render(request, 'bloguinho/index.html')

def new(request):
    return render(request, 'bloguinho/new.html')

def about(request):
    return render(request, 'bloguinho/about.html')
from django.utils import timezone
from django.shortcuts import render
from .models import NewPost
from .forms import NewForm

def index(request):
    now = timezone.now()
    posts = NewPost.objects.filter(expires__gte=now).order_by('-date')
    return render(request, 'bloguinho/index.html', {'posts': posts})


def about(request):
    return render(request, 'bloguinho/about.html')


def new(request):

    success = False

    if request.method == 'POST':
        form = NewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success = True
    else:
        form = NewForm()
    return render(request, 'bloguinho/new.html', {'form': form, 'success': success})
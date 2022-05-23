from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = PostForm()
        return render(request, 'form.html', {'form':form})

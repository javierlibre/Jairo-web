from django.shortcuts import render
from .models import *

# Create your views here.

def inicio(request):
    images = Image.objects.filter().order_by('-date_created')[:4]
    context = {}
    context['images'] = images
    return render(request, 'inicio.html', context)

def galeria(request):
    categories = Category.objects.all()
    images = Image.objects.all()
    for x in images:
        x.shashtags = x.hashtags.replace("#", "")

    context = {}
    context['categories'] = categories
    context['images'] = images
    
        
    return render(request, 'galeria.html', context)

def nosotros(request):
    return render(request, 'nosotros.html')

def blog(request):
    blogs = Blog.objects.all()
    
    for x in blogs:
        x.shortDescription = x.description[:130]

    context ={}
    context['blogs'] = blogs
    

    return render(request, 'blog.html', context)

    

def contacto(request):
    return render(request, 'contacto.html')


from django.shortcuts import render, redirect, HttpResponse
from .forms import URLForm
from .parser import parser, save
# Create your views here.

def start(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        parser(str(request.POST.get("URL", 1)))
        return redirect('/download')
    else:
        form = URLForm()

    return render(request, 'start.html', {
        'form':form
    })

def end(request):
   # if request.method == 'GET':
      #  save()
    return render(request, 'download.html')
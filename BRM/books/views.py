from django.shortcuts import render

from .forms import BookForm
# Create your views here.

def index(request):
    return render(request,'books/index.html',{'form':BookForm})


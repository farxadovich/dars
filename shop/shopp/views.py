
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Mahsulot, Toifa


def index(request):
    mahsulotlar = Mahsulot.objects.all()
    toifalar = Toifa.objects.all()
    return render(request, 'shopp/index.html', {'toifalar': toifalar, 'mahsulotlar': mahsulotlar})


def home(request):
    return render(request, 'shopp/home.html',)





from django.shortcuts import render
# Create your views here.
from .models import Projet


def index(request):
    #return HttpResponse('Hello word')
    listP=Projet.objects.all()
    return render(request,'index.html',{'listP':listP})
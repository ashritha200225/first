from django.shortcuts import render
from my_app.models import *
# Create your views here.
so=Students.objects.all()
def home(request):
    return render(request,'index.html',{'so':so})


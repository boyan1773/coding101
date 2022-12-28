from django.shortcuts import render
import pandas as pd 
# Create your views here.
def course(request):
    
    return render(request,'index.html',locals())
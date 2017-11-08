from django.http import HttpResponse
from django.shortcuts import render
import random
# Create your views here.
def home(request):
    
    # return HttpResponse(html_)
    num  =random.randint(0,10000000)
    some_list = [num,random.randint(0,1000000),random.randint(0,1000000)]
    context = {"bool_item":False,
                "num":num,
                "some_list":some_list}
    return render(request,"home.html",context)

def about(request):
    context = {}
    return render(request,"about.html",context)

def contact(request):
    context = {}
    return render(request,"contact.html",context)
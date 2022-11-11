from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
    #return HttpResponse("Hello world!")

def about(request):
    #return HttpResponse("This is about")
    return render(request, 'about.html')
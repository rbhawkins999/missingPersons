from django.shortcuts import render
from django.shortcuts import render

def indexPageView(request) :
    return render(request, 'persons/index.html')
# Create your views here.

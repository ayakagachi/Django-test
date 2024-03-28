from django.shortcuts import render
from django.http import HttpResponse

# home_page = None
def home_page(request):
    return render(request,'home.html')

# Create your views here.

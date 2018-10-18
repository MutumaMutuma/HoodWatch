from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt

# Create your views here.
def index(request):
    date = dt.date.today()
    return render(request, 'index.html',{"date":date})

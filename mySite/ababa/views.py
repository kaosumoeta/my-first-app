from django.shortcuts import render
from .models import Asmr

def index(request):
    asmrs = Asmr.objects.order_by('name')
    return render(request, 'asmr/index.html', {'asmrs':asmrs})


# Create your views here.

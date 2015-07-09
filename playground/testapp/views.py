from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
from .models import Line
from django.contrib.auth.decorators import login_required

def home(request):
    return render_to_response ("testapp/home.html",{'lines': Line.objects.all()})
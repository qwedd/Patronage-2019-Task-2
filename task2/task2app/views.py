from django.shortcuts import render
from .models import Salary
# Create your views here.

def index(request):
    return render(request, 'index.html',)

def home(request):
    all_salary = Salary.objects.all()
    return render(request, 'home.html', {'all_salary': all_salary})
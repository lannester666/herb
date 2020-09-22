from django.shortcuts import render
from django.test import TestCase

# Create your tests here.
from app.models import Incubator
import os
import django

os.environ.setdefault('DJANGO_SETTING_MODULE', 'zhiyao.settings')
django.setup()

def getIncubator_(request):
    incubator1 = Incubator.objects.all()
    for inc in incubator1:
        print(inc)
    context = {
        'incubator1': incubator1,
    }
    return render(request, 'templates/Backend.html', context)


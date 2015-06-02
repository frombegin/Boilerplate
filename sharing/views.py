from django.http import HttpResponse
from django.shortcuts import render
from sharing import models

# Create your views here.
def index(request):
    for item in models.SharingItem.objects.all():
        print item.id
        print item.name
        print item.description
    return HttpResponse(u'hello sharing!')
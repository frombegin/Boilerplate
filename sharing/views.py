from django.shortcuts import render

from sharing import models
import time
import datetime

# Create your views here.
def index(request):
    for item in models.Item.objects.all():
        print item.id
        print item.name
        print item.description
        print item

    item = models.Item.objects.create()
    item.name = 'hello'
    item.description = 'longlong string'
    item.save()
    print 'new id:', item.id, item.pk

    return render(request, 'index.html', context={
        'objects': models.Item.objects.all(),
        'time': datetime.datetime.now(),
    })
    # return HttpResponse(u'hello sharing!')

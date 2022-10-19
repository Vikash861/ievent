
from django.shortcuts import render, HttpResponse
from django.contrib import messages
from home import form
from home import models


# Create your views here.


def index(request):
        allEvents = models.Event.objects.all().values()
        context = {'events':allEvents}
        return render(request, 'index.html',context)



def host(request):
        eventForm = form.EventForm(data=request.POST,files=request.FILES)
        if eventForm.is_valid():
                eventForm.save()
                messages.success(request, 'Your Event has been hosted')
        return render(request,'host.html')


def updateFav(request,id):

        event = models.Event.objects.get(sr_no=id)
        if event.is_liked == True:
                event.is_liked = False
        else:
                event.is_liked = True

        event.save()
        return HttpResponse('success')




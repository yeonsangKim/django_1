from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from accountapp.models import NEWMODEL
from django.urls import reverse


def hello_world(request):
    if request.method =="POST":

        temp=request.POST.get('input_text')
        model_instance=NEWMODEL()
        model_instance.text=temp
        model_instance.save()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        data_list=NEWMODEL.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list' : data_list})

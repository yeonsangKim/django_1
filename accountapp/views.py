import self as self
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import NEWMODEL
from django.urls import reverse, reverse_lazy

from accountapp.decorators import account_ownership_required


@login_required                     #(login_url=reverse_lazy('accountapp:login'))
def hello_world(request):



    if request.method =="POST":

        temp=request.POST.get('input_text')
        model_instance=NEWMODEL()
        model_instance.text=temp
        model_instance.save()
        return HttpResponseRedirect(reverse('accountapp:hello_world'))      ##class와 function은 불러오는 방식이 달라서 reverse_

    else:
        data_list=NEWMODEL.objects.all()
        return render(request, 'accountapp/hello_world.html',context={'data_list' : data_list})





class AccountCreateView(CreateView):        #회원가입 해주는 logic
    model = User
    form_class = UserCreationForm
    success_url =reverse_lazy('accountapp:hello_world')  #class와 function은 불러오는 방식이 달라서 reverse_lazy
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):            #내정보 보여주는 로직
    model = User
    context_object_name = 'target_user'             #target_user룰 통해 연결해준다
    template_name = 'accountapp/detail.html'


has_ownership = [login_required, account_ownership_required]

@method_decorator(has_ownership, 'get')     #AccountUpdateView를 method로 변경login_required를 받아서
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model=User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')        #hello world로 돌아가라
    template_name = 'accountapp/update.html'



     #AccountUpdateView를 method로 변경login_required를 받아서
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')

class AccountDeleteView(DeleteView):
    model=User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'





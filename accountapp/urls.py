from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name='accountapp'
urlpatterns = [             #라우팅
    path('hello_world/', hello_world, name='hello_world'),      #html 젤 뒤에 helloworld입력시에 path

    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
            name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),          #views.py에 create에 접근할 시에,

    path('detail/<int:pk>', AccountDetailView.as_view(),name='detail')

    #path(9000/accounts/ ~~~ ==> path(detail/
    #pk라는 이름에 숫자를 받는다 (primary key)


]

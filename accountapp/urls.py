from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name='accountapp'
urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),      #html 젤 뒤에 helloworld입력시에 path

    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
            name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create')          #views.py에 create에 접근할 시에,
]

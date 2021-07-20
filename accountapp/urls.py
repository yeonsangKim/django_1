from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, \
    AccountUpdateView, AccountDeleteView  # 라우팅( name뒤에 logout,create,detail등을 urll에입력하면 해당 페이지로 이동

app_name='accountapp'
urlpatterns = [             #라우팅
    path('hello_world/', hello_world, name='hello_world'),      #html 젤 뒤에 helloworld입력시에 path

    path('login/', LoginView.as_view(template_name='accountapp/login.html'),
            name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),          #views.py에 create에 접근할 시에,

    path('detail/<int:pk>', AccountDetailView.as_view(),name='detail'),

    path('update/<int:pk>', AccountUpdateView.as_view(),name='update'),

    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

    #path(9000/accounts/ ~~~ ==> path(detail/
    #pk라는 이름에 숫자를 받는다 (primary key)


]

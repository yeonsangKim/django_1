from django.urls import path
from django.views import View

from subscribeapp.views import SubscriptionListView, SubscriptionView

app_name='subscribeapp'

urlpatterns = [
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe'),
    path('list/', SubscriptionListView.as_view(), name='list')

]
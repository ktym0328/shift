from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('mainte_list', views.mainte_list.as_view(), name='mainte_list'),
    path('incident_list', views.incident_list.as_view(), name='incident_list'),
    path('inquiry_list', views.inquiry_list.as_view(), name='inquiry_list'),
    path('request_list', views.request_list.as_view(), name='request_list')

    ]

from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('mainte_list', views.mainte_list.as_view(), name='mainte_list'),
    path('incident_list', views.incident_list.as_view(), name='incident_list'),
    path('inquiry_list', views.inquiry_list.as_view(), name='inquiry_list'),
    path('request_list', views.request_list.as_view(), name='request_list'),
    path('system_list', views.system_list.as_view(), name='system_list'),
    path('category_list', views.category_list.as_view(), name='category_list'),
    path('status_list', views.status_list.as_view(), name='status_list'),
    path('system/detail/<int:pk>/', views.system_detail.as_view(), name='system_detail'),


    ]

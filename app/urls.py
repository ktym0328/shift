from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('incident/<int:id>', views.IncidentDetailView.as_view(), name='incident_detail'),
    
    ]

from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.IncidentIndexView.as_view(), name='IncidentIndex'),
    path('incident/<int:id>', views.IncidentDetailView.as_view(), name='incident_detail'),
    
    ]

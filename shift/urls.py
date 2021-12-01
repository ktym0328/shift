"""
Definition of urls for shift.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.conf import include
from django.views.generic import View
from app import views, forms



urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('contact/', views.contact.as_view(), name='contact'),
    path('about/', views.about.as_view(), name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
]

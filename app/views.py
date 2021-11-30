"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.views import generic
from django.views.generic.base import TemplateView
from app.models import IncidentArticle, InquiryArticle, InformationArticle, OffmonitorArticle, RequestArticle


class home(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'katayama\'s App Page.'
        context['year'] = datetime.now()

        return context


class contact(TemplateView):
    template_name = 'app/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "title": "Cotntact",
            "message": "Your contact page.",
            "year": datetime.now().year,
            }

        return context


class about(TemplateView):
   template_name = 'app/about.html'

   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context = {
           'title': 'About',
           'message': 'アプリケーションに関する詳細情報を記載',
           'year': datetime.now().year          
           }
       return context


class IncidentIndexView(generic.ListView):
    template_name = 'app/incident_index.html'
    context_object_name = 'incident_list'
    queryset = IncidentArticle.objects.all()


class IncidentDetailView(generic.DetailView):
    model = IncidentArticle
    template_name = 'app/incident_detail.html'
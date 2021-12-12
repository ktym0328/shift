"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.views import generic
from django.views.generic import TemplateView, DetailView,ListView

from app.models import statuses_info, incidents_info, categories_info, systems_info, escalates_info, attachments_info, templates_info


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

class mainte_list(TemplateView):
    template_name = 'app/mainte_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'title': '非監視依頼',
            'message': '非監視依頼を管理するページ',
            'year': datetime.now().year
            }
        return context

class incident_list(TemplateView):
    template_name = 'app/incident_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'title': '故障チケット',
            'message': '故障チケットを管理するページ',
            'year': datetime.now().year
            }
        return context


class inquiry_list(TemplateView):
    template_name = 'app/inquiry_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'title': '問い合わせチケット',
            'message': '問い合わせを管理するページ',
            'year': datetime.now().year
            }
        return context

class request_list(TemplateView):
    template_name = 'app/request_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'title': '作業依頼チケット',
            'message': '作業依頼を管理するページ',
            'year': datetime.now().year
            }
        return context


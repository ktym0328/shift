"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.views import generic
from app.models import IncidentArticle, InquiryArticle, InformationArticle, OffmonitorArticle, RequestArticle

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Katayama\'s App  Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


class IndexView(generic.ListView):
    template_name = 'app/incident_index.html'
    context_object_name = 'incident_list'
    queryset = IncidentArticle.objects.all()


class IncidentDetailView(generic.DetailView):
    model = IncidentArticle
    template_name = 'app/incident_detail.html'
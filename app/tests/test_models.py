from django.test import TestCase
from app.models import Attachmaents, IncidentArticle, SystemInfo

class SystemInfoModelTests(TestCase):

    def test_is_empty(self):
        saved_systeminfo = SystemInfo.objects.all()
        self.assertEqual(saved_systeminfo.count(), 0)


    def test_sysnfo_samplecount(self):
        sysinfo = SystemInfo(id=1, system_name='sample system 1', system_detail='system detail', system_enabled='1')
        sysinfo.save()
        sysinfo = SystemInfo(id=2, system_name='sample system 2', system_detail='system detail 2', system_enabled='1')
        sysinfo.save()
        sysinfo = SystemInfo(id=3, system_name='sample system 3', system_detail='system detail 3', system_enabled='0')
        sysinfo.save()
        sysinfo = SystemInfo(id=4, system_name='sample system 4', system_detail='system detail 4', system_enabled='0')
        sysinfo.save()
        saved_systeminfo = SystemInfo.objects.all()
        self.assertEqual(saved_systeminfo.count(),4)


class AttachmentModelTests(TestCase):

    def attachment_is_empty(self):
        saved_attachment = Attachmaents.objects.all()
        self.assertEqual(saved_attachment.count(), 0)


class IncidentArticleModelTests(TestCase):

    def test_is_empty(self):
        saved_incident = IncidentArticle.objects.all()
        self.assertEqual(saved_incident.count(),0)

    def test_incident_samplecount(self):
        SystemInfoModelTests.test_sysnfo_samplecount(self)  
        incidents = IncidentArticle(id=1, incident_id='1', subject='sample subject 1', detail='sample detail', history="history 1", system_id="1")
        incidents.save()
        incidents = IncidentArticle(id=2, incident_id='2', subject='sample subject 2', detail='sample detail', history="history 2", system_id="2")
        incidents.save()
        incidents = IncidentArticle(id=3, incident_id='3', subject='sample subject 3', detail='sample detail', history="history 3", system_id="3")
        incidents.save()
        incidents = IncidentArticle(id=4, incident_id='4', subject='sample subject 4', detail='sample detail', history="history 4", system_id="4")
        incidents.save()
        saved_incidents = IncidentArticle.objects.all()
        self.assertEqual(saved_incidents.count(),4)


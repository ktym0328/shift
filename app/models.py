"""
Definition of models.
"""

from django.db import models
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.
#方針として各種別ごとのtableを分割するか、基本事項はすべて同じテーブルにして、付属品だけ別テーブルに切り出すか・・
#テーブルは種別ごとに分けたほうがいいのかな・・・おんなじ定義を繰り返しそうだけど・・・・

class IncidentArticle(models.Model):
    incident_id = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    publish_start_date = models.DateTimeField()
    publish_end_date = models.DateTimeField()
    lastupdate_date = models.DateTimeField(default=timezone.now)
    escalate_date = models.DateTimeField()

    subject = models.TextField()
    detail = models.TextField()
    history = models.TextField()
    delay_code = models.CharField(max_length=2)
    delay_reason = models.CharField(max_length=400)
    alert_count = models.IntegerField()


class InquiryArticle(models.Model):
    incident_id = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    publish_start_date = models.DateTimeField()
    publish_end_date = models.DateTimeField()
    lastupdate_date = models.DateTimeField(default=timezone.now)
    escalate_date = models.DateTimeField()

    subject = models.TextField()
    detail = models.TextField()
    history = models.TextField()

class RequestArticle(models.Model):
    incident_id = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    publish_start_date = models.DateTimeField()
    publish_end_date = models.DateTimeField()
    lastupdate_date = models.DateTimeField(default=timezone.now)
    escalate_date = models.DateTimeField()

    subject = models.TextField()
    detail = models.TextField()
    history = models.TextField()

class OffmonitorArticle(models.Model):
    incident_id = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    publish_start_date = models.DateTimeField()
    publish_end_date = models.DateTimeField()
    lastupdate_date = models.DateTimeField(default=timezone.now)

    subject = models.TextField()
    detail = models.TextField()
    history = models.TextField()


class InformationArticle(models.Model):
    incident_id = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    publish_start_date = models.DateTimeField()
    publish_end_date = models.DateTimeField()
    lastupdate_date = models.DateTimeField(default=timezone.now)

    subject = models.TextField()
    detail = models.TextField()
    history = models.TextField()


class SystemInfo(models.Model):
    system_name = models.CharField(max_length=400)
    system_detail = models.TextField
"""
Definition of models.
"""

from django.db import models
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.
#���j�Ƃ��Ċe��ʂ��Ƃ�table�𕪊����邩�A��{�����͂��ׂē����e�[�u���ɂ��āA�t���i�����ʃe�[�u���ɐ؂�o�����E�E
#�e�[�u���͎�ʂ��Ƃɕ������ق��������̂��ȁE�E�E����Ȃ���`���J��Ԃ����������ǁE�E�E�E

class SystemInfo(models.Model):
    id = models.AutoField(primary_key=True)
    system_name = models.CharField(max_length=400)
    system_detail = models.TextField(blank=True,null=True)
    system_enabled = models.BooleanField(default="1")



class IncidentArticle(models.Model):
    id = models.AutoField(primary_key=True)
    incident_id = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
    publish_start_date = models.DateTimeField(blank=True, null=True)
    publish_end_date = models.DateTimeField(blank=True, null=True)
    lastupdate_date = models.DateTimeField(auto_now=True)
    escalate_date = models.DateTimeField(blank=True,null=True)

    subject = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    delay_code = models.CharField(max_length=2 ,blank=True, null=True)
    delay_reason = models.CharField(max_length=400,blank=True, null=True)
    alert_count = models.IntegerField(blank=True,null=True)
    system = models.ForeignKey(SystemInfo, on_delete=models.PROTECT, blank=True, null=True)


class InquiryArticle(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    incident_id = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    publish_start_date = models.DateTimeField()
    publish_end_date = models.DateTimeField()
    lastupdate_date = models.DateTimeField(default=timezone.now)

    subject = models.TextField()
    detail = models.TextField()
    history = models.TextField()


class InformationArticle(models.Model):
    id = models.AutoField(primary_key=True)
    incident_id = models.CharField(max_length=200)
    create_date = models.DateTimeField(default=timezone.now)
    publish_start_date = models.DateTimeField()
    publish_end_date = models.DateTimeField()
    lastupdate_date = models.DateTimeField(default=timezone.now)

    subject = models.TextField()
    detail = models.TextField()
    history = models.TextField()


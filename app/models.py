"""
Definition of models.
"""

from django.db import models
from django.db.models.base import Model
from django.utils import timezone

# Create your models here.
#方針として各種別ごとのtableを分割するか、基本事項はすべて同じテーブルにして、付属品だけ別テーブルに切り出すか・・
#テーブルは種別ごとに分けたほうがいいのかな・・・おんなじ定義を繰り返しそうだけど・・・・

class statuses_info(models.Model):
    id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=400)
    status_memo = models.TextField(blank=True,null=True)
    status_enable = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class systems_info(models.Model):
    id = models.AutoField(primary_key=True)
    system_name = models.CharField(max_length=400)
    system_memo = models.TextField(blank=True,null=True)
    system_enable = models.BooleanField(default=True)
    system_code = models.CharField(max_length=400, blank=True,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class categories_info(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=400)
    category_memo = models.TextField(blank=True,null=True)
    category_enable = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class incidents_info(models.Model):
    id = models.AutoField(primary_key=True)
    system_id = models.ForeignKey(systems_info,on_delete=models.PROTECT)
    status_id = models.ForeignKey(statuses_info, on_delete=models.PROTECT)
    category_id = models.ForeignKey(categories_info, on_delete=models.PROTECT)
    incident_id = models.CharField(max_length=300)
    subject = models.CharField(max_length=10000)
    detail = models.TextField(blank=True,null=True)
    timeline = models.TextField(blank=True,null=True)
    escalate = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    publish_start = models.DateTimeField(blank=True,null=True)
    publish_end = models.DateTimeField(blank=True,null=True)

class escalates_info(models.Model):
    id = models.AutoField(primary_key=True)
    incident_id = models.ForeignKey(incidents_info, on_delete=models.PROTECT)
    category_name = models.CharField(max_length=400)
    category_memo = models.TextField(blank=True,null=True)
    category_enable = models.BooleanField(default=True)
    escalate_time = models.DateTimeField()
    escalate_delay_flg = models.BooleanField(default=False)
    escalate_memo = models.TextField(blank=True,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class attachments_info(models.Model):
    id = models.AutoField(primary_key=True)
    incident_id = models.ForeignKey(incidents_info, on_delete=models.PROTECT)
    attachment_name = models.CharField(max_length=10000)
    attachment_body = models.FileField()
    attachment_memo = models.TextField(blank=True,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class templates_info(models.Model):
    id = models.AutoField(primary_key=True)
    template_name = models.CharField(max_length=400)
    subject = models.CharField(max_length=10000, blank=True,null=True)
    detail = models.TextField(blank=True,null=True)
    timeline = models.TextField(blank=True,null=True)
    template_memo = models.TextField(blank=True,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


from django.contrib import admin
from app.models import IncidentArticle, InquiryArticle, InformationArticle, RequestArticle, OffmonitorArticle     #���̕�����ǉ�


admin.site.register(IncidentArticle)
admin.site.register(InquiryArticle)
admin.site.register(InformationArticle)
admin.site.register(RequestArticle)
admin.site.register(OffmonitorArticle)

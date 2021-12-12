
from django.contrib import admin
from app.models import statuses_info,systems_info,categories_info,incidents_info,escalates_info,attachments_info,templates_info


admin.site.register(statuses_info)
admin.site.register(systems_info)
admin.site.register(categories_info)
admin.site.register(incidents_info)
admin.site.register(escalates_info)
admin.site.register(attachments_info)
admin.site.register(templates_info)
from django.contrib import admin
from .models import Visitor, Question


admin.site.site_header = "Slido App Admin"

admin.site.register(Visitor)
admin.site.register(Question)

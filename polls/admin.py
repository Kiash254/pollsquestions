from dataclasses import fields
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header="Polls Admin Panel"
admin.site.site_title="polls Admin Panel Area"
admin.site.index_title="Welcome to admin panel"
class choiceinline(admin.TabularInline):
    model=Choice
    extra=3

class QeustionAdmin(admin.ModelAdmin):
    fieldsets =[(None,{"fields":['quiz_text']}),
    ('DAte Information',{'fields':['pub_date'],'classes':['collapse']}),
    ] 
    inlines=[choiceinline]

admin.site.register(Questions,QeustionAdmin)

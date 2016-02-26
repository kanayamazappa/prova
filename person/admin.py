# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Person, Log

class PersonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Person,PersonAdmin)

class LogAdmin(admin.ModelAdmin):
    list_display_links = ('owner',)
    list_display = ('owner', 'person', 'action', 'register',)
admin.site.register(Log,LogAdmin)
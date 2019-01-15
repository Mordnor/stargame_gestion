# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
   list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'slug')
   search_fields = ('first_name', 'last_name', 'phone', 'email')


class SheetAdmin(admin.ModelAdmin):
   list_display = ('id', 'customer', 'reason', 'resolution', 'comment', 'date')
   search_fields = ('customer', 'reason', 'resolution', 'comment', 'date')

class RequestAdmin(admin.ModelAdmin):
   list_display = ('id', 'customer', 'reason', 'date')
   search_fields = ('customer', 'reason', 'date')



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Sheet, SheetAdmin)
admin.site.register(Request, RequestAdmin)
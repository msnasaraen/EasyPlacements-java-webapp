# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Role,AdminDetails
from django.contrib import admin
# Register your models here.

admin.site.register(Role)
admin.site.register(AdminDetails)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Role,AdminDetails,UserDetails
from django.contrib import admin
# Register your models here.

admin.site.register(Role)
admin.site.register(AdminDetails)
admin.site.register(UserDetails)

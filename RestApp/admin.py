# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Snippet)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Institute)

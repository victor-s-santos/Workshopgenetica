from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.site_header = 'Workshop de Genética'

admin.site.unregister(Group)

# Register your models here.

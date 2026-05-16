from django.contrib import admin
from .models import Project, contacts

admin.site.register(Project)
from .models import contacts

admin.site.register(contacts)

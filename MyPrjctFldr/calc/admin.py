from django.contrib import admin

# Register your models here.
from .models import Framework, Sent_File

admin.site.register(Framework)
admin.site.register(Sent_File)
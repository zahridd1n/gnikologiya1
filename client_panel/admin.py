from django.contrib import admin
from .models import *


admin.site.register(user.User)


@admin.register(about.About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'profession')



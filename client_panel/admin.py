from django.contrib import admin
from .models import *

admin.site.register(about.About)
admin.site.register(user.User)
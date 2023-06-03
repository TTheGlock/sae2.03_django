from django.contrib import admin

# Register your models here.

from .models import Machine
from .models import Personnel

admin.site.register(Machine)
admin.site.register(Personnel)

admin.site.site_url = "http://127.0.0.1:8000/computerApp"
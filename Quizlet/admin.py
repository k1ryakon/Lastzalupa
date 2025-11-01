from django.contrib import admin

# Register your models here.
from .models import Dummy, Answer

admin.site.register(Dummy)
admin.site.register(Answer)

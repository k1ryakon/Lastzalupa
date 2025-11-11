from django.contrib import admin

# Register your models here.
from .models import Quiz, Question, Comment

admin.site.register(Quiz)
admin.site.register(Question)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name',  'body']

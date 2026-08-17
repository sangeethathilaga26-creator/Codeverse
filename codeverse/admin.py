from django.contrib import admin
from .models import Topic
from .models import Progress

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'order', 'created_at', 'updated_at')
    ordering = ('year', 'order')

admin.site.register(Topic, TopicAdmin)
admin.site.register(Progress)
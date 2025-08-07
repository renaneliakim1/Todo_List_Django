from django.contrib import admin
#registrar os models 

from .models import Tasks

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display=("title", "done", "created_at")
    list_filter = ("done",)
    search_fields= ("title",)

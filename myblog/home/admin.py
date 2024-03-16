from django.contrib import admin

from .models import Blog

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    '''Admin View for Blog'''

    list_display = ['id','title','desc']
   
from django.contrib import admin
from .models import Course, Resource, File, Session, Batch

# Register your models here.

# Models = [Student, Teacher]
# admin.site.register(Models)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = ['title']


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['course']
    list_display = ['title', 'course']
    list_filter = ['title', 'course']
    list_select_related = ['course']
    search_fields = ['title', 'course']


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['course', 'session']
    list_display = ['title', 'session', 'course']
    list_filter = ['title', 'session', 'course']
    list_select_related = ['course', 'session']
    search_fields = ['title', 'course', 'session']


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'course', 'session', 'posted_on']
    list_filter = ['title', 'course', 'author', 'session', 'batches', 'posted_on']
    list_select_related = ['author', 'course', 'session']
    search_fields = ['title', 'content', 'author', 'course', 'session', 'batches']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['title', 'id', 'resource']
    list_filter = ['resource']
    list_select_related = ['resource']
    search_fields = ['resource']

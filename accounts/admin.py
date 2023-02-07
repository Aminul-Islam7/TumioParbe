from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Admin, User, Student, Teacher

# Register your models here.


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     fields = ['first_name', 'last_name', "username", 'email', 'phone',
#               "password", 'is_admin', 'is_teacher', 'is_student', "is_active",
#               "is_staff", "is_superuser", "groups", "user_permissions",
#               "last_login", "date_joined"]

#     filter_horizontal = ("groups", "user_permissions")
#     pass


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {
         "fields": ("first_name", "last_name", "email", 'phone')}),
        (
            ("Permissions"),
            {
                "fields": (
                    'is_student',
                    'is_teacher',
                    'is_admin',
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


@ admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__']


@ admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__']


@ admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__']

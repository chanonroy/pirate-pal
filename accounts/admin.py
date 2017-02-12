from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

# Define an inline admin descriptor
class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserInline, )

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

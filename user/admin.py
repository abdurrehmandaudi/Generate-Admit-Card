from django.contrib import admin
from .models import UserDetail

# Register your models here.

@admin.register(UserDetail)
class UserDetailAdmin(admin.ModelAdmin):
    list_display=('user_id','username','enroll_no','roll_no','mobile','photo')
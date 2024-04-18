from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import MedUser

@admin.register(MedUser)
class AdminMedUser(admin.ModelAdmin):
    list_display = ["specialization", "full_name"]
    search_fields = ["first_name", "last_name"]



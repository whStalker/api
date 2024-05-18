from django.contrib.auth.hashers import make_password
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import MedUser, Diagnos

@admin.register(MedUser)
class AdminMedUser(admin.ModelAdmin):
    list_display = ["specialization", "full_name", "role"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["role"]

    def save_model(self, request, obj, form, change) -> None:
        obj.password = make_password(obj.password)
        return super().save_model(request, obj, form, change)

admin.site.register(Diagnos)

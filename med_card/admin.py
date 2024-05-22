from django.contrib.auth.hashers import make_password
from django.contrib import admin
from .models import MedUser, Diagnos

class DiagnosInline(admin.TabularInline):
    model = Diagnos
    extra = 0
    fk_name = "user"
    verbose_name = "Диагноз"
    verbose_name_plural = "Диагнозы"


@admin.register(MedUser)
class AdminMedUser(admin.ModelAdmin):
    list_display = ["specialization", "full_name", "role"]
    search_fields = ["first_name", "last_name"]
    list_filter = ["role"]
    inlines = [DiagnosInline]

    def save_model(self, request, obj, form, change) -> None:
        obj.password = make_password(obj.password)
        return super().save_model(request, obj, form, change)


admin.site.register(Diagnos)

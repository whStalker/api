from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class MedRole(models.TextChoices):
    DOCTOR = "doctor", "Доктор"
    PATIENT = "patient", "Пациент"


class MedUser(User):
    role = models.CharField("Роль", choices=MedRole.choices, max_length=128, null=True, blank=True)
    specialization = models.CharField("Специализация", max_length=128, null=True, blank=True)

    @property
    def full_name(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}"

        return self.first_name

    def __str__(self) -> str:
        return f"{self.role} - {self.full_name}"


class Diagnos(models.Model):
    user = models.ForeignKey(verbose_name="Пациент", to=MedUser, on_delete=models.DO_NOTHING, related_name="diagnos")
    doctor = models.ForeignKey(verbose_name="Имя доктора", to=MedUser, on_delete=models.DO_NOTHING, related_name="diagnos_doctor")
    title = models.CharField('Название болезни', max_length=128)
    description = models.TextField('Описание болезни')

    def __str__(self):
        return self.title


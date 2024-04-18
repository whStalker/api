from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class MedSpecialization(models.TextChoices):
    DOCTOR = "doctor", "Доктор"


class MedUser(User):
    specialization = models.CharField("специализация", choices=MedSpecialization.choices, max_length=128)

    @property
    def full_name(self):
        if self.last_name:
            return f"{self.first_name} {self.last_name}"

        return self.first_name

    def __str__(self) -> str:
        return f"{self.specialization} - {self.full_name}"

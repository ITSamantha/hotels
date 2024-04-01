from django.db import models


class Sex(models.TextChoices):
    FEMALE = 'F', 'Female'
    MALE = 'M', 'MALE'

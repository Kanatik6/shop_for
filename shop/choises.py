from django.db import models

class GenderChoise(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DETI = 'deti'

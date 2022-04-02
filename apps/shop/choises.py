from django.db import models

class GenderChoise(models.TextChoices):
    MALE = "Male"
    FEMALE = "Female"
    DETI = 'deti'


class YearChoise(models.TextChoices):
    ONE_FOUR = "1-4 лет"
    FOUR_EIGHT = '4-8 лет'
    EIGHT_THIRTEEN = '8-13 лет'

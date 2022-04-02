from django.db import models

class GenderChoise(models.TextChoices):
    MALE = "Мальчик"
    FEMALE = "Девочка"


class RaitingChoise(models.IntegerChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5 

year_choise =[(f"{x-1}-{x} года",f"{x-1}-{x} года")if x < 5 else (f"{x-1}-{x} лет",f"{x-1}-{x} лет") for x in range(1,17) ]

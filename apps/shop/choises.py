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


# class YearChoise(models.):
#     ONE = 1
#     TWO = 2
#     THREE = 3
#     FOUR = 4
#     FIVE = 5 

year_choise =[(f"{x-1}-{x}",f"{x-1}-{x}") for x in range(1,17) ]

year_values = [f"{x-1}-{x}" for x in range(1,17) ]
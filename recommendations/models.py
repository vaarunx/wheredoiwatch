from django.db import models

# Create your models here.


class Search(models.Model):
    COUNTRY_CHOICES = (
        ("India" , 'IN'),
        ("US" , "USA"),
    )
    name = models.CharField(max_length= 256)
    country = models.CharField(choices=COUNTRY_CHOICES , max_length= 256)
    
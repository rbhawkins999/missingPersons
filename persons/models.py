from django.db import models

# Create your models here.

class Person(models.Model):
    date_missing = models.DateField()
    last_name = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    age_at_missing = models.IntegerField()
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 2)
    gender = models.CharField(max_length = 1)
    race = models.CharField(max_length = 1)

    def __str__(self) :
        return '%s %s' % (self.first_name, self.last_name)
class Detail (models.Model):
    detail = models.CharField(max_length=255)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key= True)
    
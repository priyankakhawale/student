from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200,default='')
    age = models.IntegerField()

    class Meta:
        db_table='Student_Info'

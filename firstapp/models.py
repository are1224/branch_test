from django.db import models

# Create your models here.
class student(models.Model):
    class_num = models.IntegerField(default=1)
    name = models.CharField(max_length=30, default='')
    phone_num = models.CharField(max_length=30)
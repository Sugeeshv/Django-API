from django.db import models

# Create your models here.


class crud(models.Model):
    name=models.CharField(max_length=30)
    se=models.CharField(max_length=30)
    class Meta:
        db_table='crud'

from django.db import models

# Create your models here.


class Lawyer(models.Model):
    suffix = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    current = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "lawyer"
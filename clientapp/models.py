from django.db import models
from lawyerapp.models import Lawyer

# Create your models here.


class Client(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=500)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "client"


class Book_lawyer(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField(default=0)

    class Meta:
        db_table = "Book_lawyer"


class Feedback(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE, default=0)
    description = models.TextField(max_length=500)
    rating = models.CharField(max_length=100)

    class Meta:
        db_table = "client_feedback"

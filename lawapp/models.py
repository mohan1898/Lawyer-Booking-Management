from django.db import models

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField(max_length=500)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "contact"



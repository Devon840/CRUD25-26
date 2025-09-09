from django.db import models

# Create your models here.
<<<<<<< HEAD

class Record(models.Model):
    creation_data = models.DateTimeField(auto_now_add = True)

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)

def __str__(self):
    return self.first_name + "" + self.last_name
=======
class Record(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    creation_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
>>>>>>> e7e30b9bf6e4833e8f25e46e9acad501b9714b39

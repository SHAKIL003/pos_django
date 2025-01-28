from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Mobile(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='mobiles')
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='mobiles/', blank=True, null=True)

    def __str__(self):
        return self.name

class Specification(models.Model):
    mobile = models.OneToOneField(Mobile, on_delete=models.CASCADE, related_name='specifications')
    processor = models.CharField(max_length=100)
    ram = models.IntegerField()
    storage = models.CharField(max_length=50)
    battery = models.IntegerField()
    screen_size = models.FloatField()
    camera = models.CharField(max_length=100)
    os = models.CharField(max_length=50)

    def __str__(self):
        return f"Specifications of {self.mobile.name}"

from django.db import models
from django.urls import reverse
# Create your models here.
class City(models.Model):
    city = models.CharField(max_length=120) # max_length = required
    location = models.CharField(max_length=120) # max_length = required
    code = models.CharField(max_length=500) # max_length = required

class Room(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    floor       = models.IntegerField()
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    water = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    description     = models.TextField(blank=False, null=False)
    views = models.CharField(max_length=120)
    blocked = models.BooleanField(default=False)
    public = models.BooleanField(default=False)
    private = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"
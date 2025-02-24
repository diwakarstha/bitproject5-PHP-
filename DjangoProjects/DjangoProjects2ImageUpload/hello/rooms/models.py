from django.db import models
from django.urls import reverse
# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=120) # max_length = required

    def __str__(self):
        return self.name

class Location(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    location = models.CharField(max_length=120) # max_length = required
    code = models.CharField(max_length=500) # max_length = required

    def __str__(self):
        return self.location

class Room(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    house_number = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    floor       = models.IntegerField()
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    water = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    description     = models.TextField(max_length=500,blank=False, null=False)
    date_posted = models.DateField(auto_now_add=True)
    views = models.CharField(max_length=120, default="0")
    blocked = models.BooleanField(default=False)
    public = models.BooleanField(default=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk) + str(self.house_number)

    # def get_absolute_url(self):
    #     return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"
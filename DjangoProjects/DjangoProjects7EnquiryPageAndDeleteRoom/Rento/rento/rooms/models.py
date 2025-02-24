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
    
    @staticmethod
    def get_all_locations():
        return Location.objects.all()

class Room(models.Model):
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    house_number = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    floor       = models.IntegerField()
    price       = models.PositiveIntegerField()
    image1 = models.ImageField(upload_to='')
    image2 = models.ImageField(upload_to='')
    image3 = models.ImageField(upload_to='')
    water = models.BooleanField(default=False)
    internet = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    description     = models.TextField(max_length=500,blank=False, null=False)
    date_posted = models.DateField(auto_now_add=True)
    views = models.IntegerField(default=0)
    blocked = models.BooleanField(default=False)
    public = models.BooleanField(default=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)

    @staticmethod
    def get_all_rooms():
        return Room.objects.all()

    @staticmethod
    def get_all_rooms_by_filter(location_id):
        if location_id:
            return Room.objects.filter(location = location_id)
        else:
            return Room.get_all_rooms()

    @staticmethod
    def get_all_rooms_by_waterinternetparkingfilter(water_id,internet_id,parking_id):
            return Room.objects.filter(water = water_id, parking = internet_id, internet = parking_id)
    
    @staticmethod
    def get_all_rooms_by_allfilter(location_id,water_id,internet_id,parking_id):
            return Room.objects.filter(location = location_id,water = water_id, parking = internet_id, internet = parking_id)

    # def get_absolute_url(self):
    #     return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"
from django.db import models

class MainImage(models.Model):
    image = models.CharField(default='', max_length=255)
    

class Car(models.Model):
    title = models.CharField(max_length=255, default='', blank=True, null=True)
    price = models.CharField(max_length=255, default='', blank=True, null=True)
    year = models.CharField(max_length=255, default='', blank=True, null=True)
    millage = models.CharField(max_length=255, default='', blank=True, null=True)
    fuel_type = models.CharField(max_length=255, default='', blank=True, null=True)
    transmission = models.CharField(max_length=255, default='', blank=True, null=True)
    horsepower = models.CharField(max_length=255, default='', blank=True, null=True)
    color = models.CharField(max_length=255, default='', blank=True, null=True)
    moreInformation = models.CharField(max_length=3000, default='', blank=True, null=True)
    main_image = models.ForeignKey(MainImage, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Image(models.Model):
    image = models.CharField(max_length=255, default='')
    car = models.ForeignKey(Car,  default='', related_name='images', max_length=255, on_delete=models.CASCADE)
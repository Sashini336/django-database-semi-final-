from rest_framework import serializers
from .models import Car, MainImage, Image

class MainImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainImage
        fields = ['image']
        
class ImageSerializer(serializers.Serializer):
    image = serializers.CharField(max_length=255)

class CarSerializer(serializers.ModelSerializer):
    main_image = MainImageSerializer()
    # images = ImageSerializer()

    class Meta:
        model = Car
        fields = ['id', 'title', 'price', 'year', 'millage', 'fuel_type', 'transmission', 'horsepower', 'color', 'moreInformation', 'main_image']

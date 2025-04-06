from .models import Cams, IceCream
from rest_framework import serializers


class CamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cams
        fields = ['id','name', 'place' ]


class IceCreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = IceCream
        fields = ['id', 'name', 'code', 'camera', 'quantity', 'size_per_box' ]
        

        
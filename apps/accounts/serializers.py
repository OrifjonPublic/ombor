from .models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'role', 'password' ]
        extra_kwargs = {
            'password': {'write_only': True},  # Parol javobda ko'rinmaydi
        }
    
    def create(self, validated_data):
        # Parolni hash qilish
        validated_data['password'] = make_password(validated_data['password'])
        
        # User obyektini yaratish
        user = User.objects.create(**validated_data)
        return user

# serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Asl serializer logikasini ishga tushiramiz
        data = super().validate(attrs)
        
        # Foydalanuvchi ma'lumotlarini qo'shamiz
        user = self.user
        data['user_id'] = user.id
        data['role'] = user.role  # Bu yerda statusni o'zingizning logikangizga moslashtirasiz
        
        return data
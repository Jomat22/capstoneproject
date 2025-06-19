from rest_framework import serializers
from .models import booking, menu, MenuItem
from django.contrib.auth.models import User


class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields= "__all__"

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields ="__all__"



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MenuItemSerializer(serializers.ModelSerializer):
    """
    Serializer for the MenuItem model.
    Converts MenuItem instances to JSON and vice-versa.
    """
    class Meta:
        # Link the serializer to the MenuItem model.
        model = MenuItem
        # Include all fields from the MenuItem model in the serialization.
        fields = '__all__'



class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Booking model.

    This serializer automatically generates fields for all fields present
    in the 'booking' model.
    """
    class Meta:
        model = booking
        fields = '__all__'

from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Worker


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['post', 'worker', 'director']


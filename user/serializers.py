from rest_framework import serializers

from user.models import User


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    middle_name = serializers.CharField(required=False)
    phone = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    status = serializers.CharField(required=True)
    post = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'middle_name', 'phone', 'name', 'surname', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

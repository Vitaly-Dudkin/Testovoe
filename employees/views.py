from rest_framework import generics
from user.serializers import CreateUserSerializer, UserSerializer
from .models import Worker
from .serializers import EmployeeSerializer


class CreateEmployeeView(generics.CreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {'worker': user.id, 'director': request.user.id, 'post': request.data.get('post')}
        serializer = EmployeeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

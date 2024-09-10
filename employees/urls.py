from django.urls import path

from .apps import EmployeesConfig
from .views import CreateEmployeeView


app_name = EmployeesConfig.name

urlpatterns = [
    path('create_employee/', CreateEmployeeView.as_view(), name='create_employee'),
]


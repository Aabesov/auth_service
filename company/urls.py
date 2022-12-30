from django.urls import path
from .views import EmployeeDepartmentAPIView


urlpatterns = [
    path("departments/<int:pk>/", EmployeeDepartmentAPIView.as_view())

]

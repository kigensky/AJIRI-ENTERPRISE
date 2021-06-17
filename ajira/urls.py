from django.urls import include, path
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'profile',views.ProfileViewSet)
router.register(r'employee_salary',views.EmployeeSalaryViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]


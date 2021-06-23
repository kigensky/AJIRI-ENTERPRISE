from django.urls import path

from .views import RegisterView, LoginView, UserView, LogoutView
from django.urls import include, path
from rest_framework import routers
from .import views


router = routers.DefaultRouter()
router.register(r'profile',views.ProfileViewSet)
router.register(r'employee_salary',views.EmployeeSalaryViewset)
router.register(r'employee',views.EmployeeViewset)
router.register(r'leave',views.LeaveViewset)
urlpatterns = [
    path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls')),

    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
   
]


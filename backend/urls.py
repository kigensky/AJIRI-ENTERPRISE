"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
    #path('api/employee/',views.EmployeeList.as_view(),name='employee'),
    #path('employee/update/<name>/',views.EmployeeList.as_view(),name='update_employee'),
    #path('employee/delete/<int:pk>/',views.EmployeeList.as_view(),name='delete_employee'),
]
#if settings.DEBUG:
    #urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from . import views
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static


urlpatterns=[
  #employees urls
  path('api/employee/',views.EmployeeList.as_view(),name='employee'),
  path('employee/update/<name>/',views.EmployeeList.as_view(),name='update_employee'),
  path('employee/delete/<int:pk>/',views.EmployeeList.as_view(),name='delete_employee'),
  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
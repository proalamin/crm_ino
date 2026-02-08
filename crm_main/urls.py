from django.contrib import admin
from django.urls import path
from customer.views import student_list_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', student_list_create),
]

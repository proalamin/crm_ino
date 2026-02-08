from django.contrib import admin
from django.urls import path
from customer.views import student_list_create
from customer.views import home, customer_list_page



urlpatterns = [
    path('', home),
    path('api/students/', student_list_create),
    path('customers/', customer_list_page),

]

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Personal
from .serializers import PersonalSerializer
from django.shortcuts import render

@api_view(['GET', 'POST'])
def student_list_create(request):

    if request.method == 'GET':
        students = Personal.objects.all()
        serializer = PersonalSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def home(request):
    return render(request, "customer/index.html")
def customer_list_page(request):
    return render(request, "customer/all_customer.html")

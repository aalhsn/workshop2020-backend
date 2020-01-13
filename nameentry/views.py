from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from .models import Student
from .serializers import StudentDetailsSerializer

class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailsSerializer

class CreateStudentView(CreateAPIView):
    serializer_class = StudentDetailsSerializer
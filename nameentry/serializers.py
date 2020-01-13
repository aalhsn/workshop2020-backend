from rest_framework import serializers
from .models import Student

class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name','hobbies','date_of_birth']


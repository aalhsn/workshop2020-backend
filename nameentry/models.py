from django.db import models

# Create your models here.
class Student(models.Model):
	name= models.CharField(max_length=120)
	hobbies= models.TextField()
	date_of_birth=models.DateField()

	def __str__(self):
		return self.name
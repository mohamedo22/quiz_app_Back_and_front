from django.db import models

# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    exam_result = models.CharField(max_length=5)
    def __str__(self):
        return self.name
class teacher(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class quistions(models.Model):
    quistion = models.TextField()
    first_answer = models.TextField()
    second_answer = models.TextField()
    third_answer = models.TextField() 
    right_answer = models.TextField()
from django.db import models

# Create your models here.

class Task(models.Model):
    task_name=models.CharField(max_length=50)
    status=models.BooleanField(default=True)
    
    def __str__(self):
        return self.task_name , self.status

class Employee(models.Model):
    emp_name=models.CharField(max_length=50)
    email=models.EmailField()
    task=models.ForeignKey(Task,on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name, self.task

class Client(models.Model):
    client_name=models.CharField(max_length=50)
    area=models.CharField(max_length=50)
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    def __str__(self):
        return self.client_name, self.task
   
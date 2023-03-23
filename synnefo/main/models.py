from django.db import models
class Department(models.Model):
  Dept_name=models.CharField(max_length=100)
  def __str__(self):
    return self.Dept_name
class Batch(models.Model):
  Batch_time=models.CharField(max_length=50)
  def __str__(self):
    return self.Batch_time
class Student(models.Model):
  Std_name=models.CharField(max_length=100)
  Address=models.CharField(max_length=100)
  Dept=models.ForeignKey(Department,default=1,on_delete=models.CASCADE)
  
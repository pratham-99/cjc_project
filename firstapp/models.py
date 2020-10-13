from django.db import models


class Student(models.Model):

    rn = models.IntegerField()
    name = models.CharField(max_length=30)
    marks = models.FloatField()

    def __str__(self):
        #return f'Rn={self.rn}, Name={self.name}, Marks={self.marks}'
        return self.name

class Student_details(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    city = models.CharField(max_length=10)
    pincode = models.IntegerField()
    email = models.CharField(max_length=20)


class Employee(models.Model):
    eid = models.IntegerField()
    efirst_name = models.CharField(max_length=10)
    elast_name = models.CharField(max_length=10)
    esalary = models.FloatField()




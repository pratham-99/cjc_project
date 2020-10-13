from django.contrib import admin
from .models import Student, Employee, Student_details
# OR from . import models


class StudentAdmin(admin.ModelAdmin):
    list_display = ['rn','name','marks']
admin.site.register(Student,StudentAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid', 'efirst_name', 'esalary']
admin.site.register(Employee,EmployeeAdmin)

class Student_detailsAdmin(admin.ModelAdmin):
    list_display = ['city', 'pincode', 'email','student']
admin.site.register(Student_details,Student_detailsAdmin)
from django.contrib import admin
from.models import *
# Register your models here.
class Display_Dept(admin.ModelAdmin):
    list_display=['Dept_name']
class Display_Batch(admin.ModelAdmin):
    list_display=['Batch_time']
class Display_Student(admin.ModelAdmin):
    list_display=['Std_name','Address','Dept']
admin.site.register(Department,Display_Dept)
admin.site.register(Batch,Display_Batch)
admin.site.register(Student,Display_Student)



from django.contrib import admin
from .models import *
admin.site.register(reciepes)
admin.site.register(StudentId)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Subject)
class SubjectMarksAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']
admin.site.register(SubjectMarks,SubjectMarksAdmin)

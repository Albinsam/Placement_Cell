from django.contrib import admin
from . models import Student
# Register your models here.
from .models import LoginRecord

admin.site.register(LoginRecord)
admin.site.register(Student)
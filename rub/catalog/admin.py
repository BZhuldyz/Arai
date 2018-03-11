from django.contrib import admin

# Register your models here.
from .models import kafedra,Prepod,Student

admin.site.register(kafedra)
admin.site.register(Prepod)
admin.site.register(Student)


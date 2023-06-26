from django.contrib import admin
from .models import Course, Day, Syllabus, Course_syllabus

# Register your models here.
admin.site.register(Course)
admin.site.register(Day)
admin.site.register(Syllabus)
admin.site.register(Course_syllabus)

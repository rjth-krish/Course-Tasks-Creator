from django.db import models

# Create your models here.


class Course(models.Model):
    Course = models.CharField(max_length=220)

    def __str__(self):
        return self.Course

    class Meta:
        verbose_name_plural = 'Course'


class Day(models.Model):
    Day = models.CharField(max_length=223)

    def __str__(self):
        return self.Day


class Syllabus(models.Model):
    Syllabus = models.CharField(max_length=220)

    def __str__(self):
        return self.Syllabus

    class Meta:
        verbose_name_plural = 'Syllabus'


class Course_syllabus(models.Model):
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Day = models.ForeignKey(Day, on_delete=models.CASCADE)
    Syllabus = models.ManyToManyField(Syllabus, blank=True)
    Percentage = models.IntegerField()

    def __str__(self):
        return self.Syllabus

    class Meta:
        verbose_name_plural = 'Course_Syllabus'

# Generated by Django 4.2.1 on 2023-06-26 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0002_alter_day_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_syllabus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Percentage', models.IntegerField()),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackerapp.course')),
                ('Day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackerapp.day')),
                ('Syllabus', models.ManyToManyField(blank=True, to='trackerapp.syllabus')),
            ],
            options={
                'verbose_name_plural': 'Course_Syllabus',
            },
        ),
    ]

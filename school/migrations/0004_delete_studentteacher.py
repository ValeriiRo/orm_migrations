# Generated by Django 4.0.4 on 2022-05-14 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_remove_student_teacher_student_teacher_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudentTeacher',
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0002_teacher_students_exam_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='quistions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quistion', models.TextField()),
                ('first_answer', models.TextField()),
                ('second_answer', models.TextField()),
                ('third_answer', models.TextField()),
                ('fourth_answer', models.TextField()),
                ('right_answer', models.TextField()),
            ],
        ),
    ]

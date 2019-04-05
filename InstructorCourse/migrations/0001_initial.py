# Generated by Django 2.1.7 on 2019-04-04 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Course.Course')),
            ],
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-27 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='name',
            new_name='Accountname',
        ),
        migrations.AddField(
            model_name='account',
            name='Accountid',
            field=models.IntegerField(default=0),
        ),
    ]

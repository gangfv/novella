# Generated by Django 4.1.2 on 2022-10-21 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_customuser_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='money',
            field=models.IntegerField(default=40000),
        ),
    ]

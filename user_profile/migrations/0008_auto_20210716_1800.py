# Generated by Django 3.1.12 on 2021-07-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_auto_20210608_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(max_length=400),
        ),
    ]

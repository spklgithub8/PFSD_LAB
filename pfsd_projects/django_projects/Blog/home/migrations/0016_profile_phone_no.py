# Generated by Django 3.1.7 on 2021-07-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210705_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
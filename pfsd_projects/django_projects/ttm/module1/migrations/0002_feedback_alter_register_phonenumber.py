# Generated by Django 4.2.8 on 2024-02-06 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=216)),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
        migrations.AlterField(
            model_name='register',
            name='phonenumber',
            field=models.PositiveBigIntegerField(),
        ),
    ]
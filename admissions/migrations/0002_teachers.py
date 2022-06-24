# Generated by Django 3.2.7 on 2022-01-10 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=20)),
            ],
        ),
    ]

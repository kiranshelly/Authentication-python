# Generated by Django 3.2.6 on 2021-09-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OTP', models.IntegerField(null=True)),
            ],
        ),
    ]
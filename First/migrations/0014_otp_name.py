# Generated by Django 3.2.6 on 2021-09-30 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0013_register_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='First.register'),
        ),
    ]

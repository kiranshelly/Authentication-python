# Generated by Django 3.2.6 on 2021-09-15 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First', '0006_rename_reg_name_otp_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
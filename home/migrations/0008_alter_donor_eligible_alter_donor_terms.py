# Generated by Django 4.0.2 on 2022-02-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='Eligible',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='donor',
            name='terms',
            field=models.BooleanField(),
        ),
    ]
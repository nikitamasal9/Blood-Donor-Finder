# Generated by Django 4.0.2 on 2022-02-24 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_usernamepasswords'),
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

# Generated by Django 4.0.2 on 2022-03-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_bhbb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bhbb',
            name='bankid',
            field=models.CharField(default='5', max_length=100),
        ),
    ]

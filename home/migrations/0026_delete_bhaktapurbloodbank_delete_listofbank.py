# Generated by Django 4.0.2 on 2022-03-03 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_alter_bhaktapurbloodbank_abminus_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BhaktapurBloodBank',
        ),
        migrations.DeleteModel(
            name='listofbank',
        ),
    ]

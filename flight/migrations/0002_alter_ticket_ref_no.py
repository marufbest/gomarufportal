# Generated by Django 4.1.6 on 2023-04-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ref_no',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]

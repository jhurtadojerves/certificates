# Generated by Django 2.2 on 2019-05-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='identification_card',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
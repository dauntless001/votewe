# Generated by Django 3.2 on 2022-04-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ward',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
# Generated by Django 4.1 on 2023-06-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensac', '0010_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='new_email',
            field=models.EmailField(max_length=50),
        ),
    ]

# Generated by Django 4.1 on 2023-06-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensac', '0006_alter_contact_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
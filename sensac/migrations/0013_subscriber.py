# Generated by Django 4.2 on 2023-06-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensac', '0012_remove_newsletter_date_added_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_mail', models.EmailField(max_length=254)),
            ],
        ),
    ]

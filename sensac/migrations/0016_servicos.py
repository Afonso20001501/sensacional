# Generated by Django 4.2 on 2023-06-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensac', '0015_rename_mew_email_newsletter_new_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
    ]

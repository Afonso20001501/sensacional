# Generated by Django 4.1 on 2023-06-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensac', '0003_rename_arq_produto_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('address_to', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]

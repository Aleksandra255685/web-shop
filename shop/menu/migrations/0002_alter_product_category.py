# Generated by Django 4.2.1 on 2023-06-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('pastry', 'pastry'), ('candy-bar', 'candy-bar'), ('cake', 'cake')], default='cake', max_length=20, verbose_name='Категория'),
        ),
    ]
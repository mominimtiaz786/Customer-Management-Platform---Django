# Generated by Django 4.0 on 2021-12-22 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-16 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='Photo'),
        ),
    ]
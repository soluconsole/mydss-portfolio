# Generated by Django 4.0.6 on 2022-08-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, upload_to='static/img'),
        ),
    ]

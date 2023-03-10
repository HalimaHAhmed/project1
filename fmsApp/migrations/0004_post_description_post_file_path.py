# Generated by Django 4.0.3 on 2023-01-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fmsApp', '0003_remove_post_description_remove_post_file_path_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='file_path',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-11 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_house', '0015_remove_file_title_remove_file_type_resource_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='title',
            field=models.CharField(default='UNTITLED', max_length=255),
            preserve_default=False,
        ),
    ]
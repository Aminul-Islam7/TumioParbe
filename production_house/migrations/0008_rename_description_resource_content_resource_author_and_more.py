# Generated by Django 4.0.6 on 2022-07-22 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('production_house', '0007_rename_resourcefile_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='description',
            new_name='content',
        ),
        migrations.AddField(
            model_name='resource',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='resource',
            name='posted_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

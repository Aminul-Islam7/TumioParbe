# Generated by Django 4.0.6 on 2022-07-22 11:26

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('production_house', '0009_file_type'),
        ('accounts', '0017_alter_admin_image_alter_admin_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='batches',
            field=smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='sessions', chained_model_field='session', related_name='students', to='production_house.batch'),
        ),
    ]

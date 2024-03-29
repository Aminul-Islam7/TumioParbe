# Generated by Django 4.0.6 on 2022-07-17 17:01

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_student_facebook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='country',
            field=django_countries.fields.CountryField(default='Bangladesh', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='flat',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='house',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

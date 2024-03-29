# Generated by Django 4.0.6 on 2022-07-16 14:41

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('production_house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('is_student', models.BooleanField(default=True)),
                ('is_teacher', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip', models.CharField(blank=True, max_length=9, null=True)),
                ('area', models.TextField(blank=True, null=True)),
                ('road', models.CharField(blank=True, max_length=5, null=True)),
                ('house', models.CharField(blank=True, max_length=5, null=True)),
                ('flat', models.CharField(blank=True, max_length=20, null=True)),
                ('batches', smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='sessions', chained_model_field='session', horizontal=True, related_name='teachers', to='production_house.batch')),
                ('courses', models.ManyToManyField(blank=True, related_name='teachers', to='production_house.course')),
                ('sessions', smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='courses', chained_model_field='course', related_name='teachers', to='production_house.session')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('birth_date', models.DateField(null=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('father_name', models.CharField(blank=True, max_length=50, null=True)),
                ('father_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('mother_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip', models.CharField(blank=True, max_length=9, null=True)),
                ('area', models.TextField(blank=True, null=True)),
                ('road', models.CharField(blank=True, max_length=5, null=True)),
                ('house', models.CharField(blank=True, max_length=5, null=True)),
                ('flat', models.CharField(blank=True, max_length=20, null=True)),
                ('batches', smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='sessions', chained_model_field='session', horizontal=True, related_name='students', to='production_house.batch')),
                ('courses', models.ManyToManyField(blank=True, related_name='students', to='production_house.course')),
                ('sessions', smart_selects.db_fields.ChainedManyToManyField(blank=True, chained_field='courses', chained_model_field='course', related_name='students', to='production_house.session')),
            ],
        ),
    ]

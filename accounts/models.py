import sys
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.auth.models import AbstractUser
from django.db import models
from smart_selects.db_fields import ChainedManyToManyField
from django_countries.fields import CountryField

# Create your models here.


def location(instance, filename):
    filebase, extension = filename.split('.')
    return 'profile_pics/%s.%s' % (instance.user.username, extension)


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    last_updated = models.DateTimeField(auto_now=True)
    # Types
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


from production_house.models import Course, Session, Batch


class Student(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True, related_name='student')
    courses = models.ManyToManyField(Course,
                                     related_name='students',
                                     blank=True)
    sessions = ChainedManyToManyField(Session,
                                      chained_field='courses',
                                      chained_model_field='course',
                                      related_name='students',
                                      blank=True)
    batches = ChainedManyToManyField(Batch,
                                     chained_field='sessions',
                                     chained_model_field='session',
                                    #  horizontal=True,
                                     related_name='students',
                                     blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    # Personal Info
    image = models.ImageField(
        default='profile_pics/default.jpg', upload_to=location, blank=True)
    birth_date = models.DateField(null=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    # Parents' Info
    father_name = models.CharField(max_length=50, null=True, blank=True)
    father_phone = models.CharField(max_length=20, null=True, blank=True)
    mother_name = models.CharField(max_length=50, null=True, blank=True)
    mother_phone = models.CharField(max_length=20, null=True, blank=True)
    # Address
    country = CountryField(blank_label='Select Country', null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip = models.CharField(max_length=9, null=True, blank=True)
    area = models.TextField(null=True, blank=True)
    road = models.CharField(max_length=5, null=True, blank=True)
    house = models.CharField(max_length=50, null=True, blank=True)
    flat = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def save(self):
        img = Image.open(self.image)
        img = img.convert('RGB')

        output = BytesIO()

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

        img.save(output, format='JPEG', quality=90)
        output.seek(0)

        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)

        super(Student, self).save()


class Teacher(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True, related_name='teacher')
    image = models.ImageField(
        default='profile_pics/default.jpg', upload_to=location, blank=True)
    birth_date = models.DateField(null=True)
    facebook = models.URLField(null=True, blank=True)
    courses = models.ManyToManyField(Course,
                                     related_name='teachers',
                                     blank=True)
    sessions = ChainedManyToManyField(Session,
                                      chained_field='courses',
                                      chained_model_field='course',
                                      related_name='teachers',
                                      blank=True)
    batches = ChainedManyToManyField(Batch,
                                     chained_field='sessions',
                                     chained_model_field='session',
                                    #  horizontal=True,
                                     related_name='teachers',
                                     blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def save(self):
        img = Image.open(self.image)
        img = img.convert('RGB')

        output = BytesIO()

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

        img.save(output, format='JPEG', quality=90)
        output.seek(0)

        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)

        super(Teacher, self).save()


class Admin(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True, related_name='admin')
    image = models.ImageField(
        default='profile_pics/default.jpg', upload_to=location, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def save(self):
        img = Image.open(self.image)
        img = img.convert('RGB')

        output = BytesIO()

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

        img.save(output, format='JPEG', quality=90)
        output.seek(0)

        self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                          sys.getsizeof(output), None)

        super(Admin, self).save()

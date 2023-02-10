from django.db import models
from accounts.models import User
from django.utils import timezone
from smart_selects.db_fields import ChainedForeignKey, ChainedManyToManyField
from tinymce.models import HTMLField
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Session(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course,
                               on_delete=models.PROTECT,
                               related_name='sessions')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Batch(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course,
                               on_delete=models.PROTECT,
                               related_name='batches')
    session = ChainedForeignKey(Session,
                                chained_field='course',
                                chained_model_field='course',
                                auto_choose=True,
                                on_delete=models.PROTECT,
                                related_name='batches')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Resource(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True, default='Untitled')
    content = HTMLField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    posted_on = models.DateTimeField(default=timezone.now)
    course = models.ForeignKey(Course,
                               on_delete=models.PROTECT,
                               related_name='resources')
    session = ChainedForeignKey(Session,
                                chained_field='course',
                                chained_model_field='course',
                                auto_choose=True,
                                on_delete=models.PROTECT,
                                related_name='resources')
    batches = ChainedManyToManyField(Batch,
                              chained_field='session',
                              chained_model_field='session',
                              horizontal=True,
                              auto_choose=True,
                              related_name='resources')
    
    file = models.FileField(upload_to='resource_files', null=True, blank=True)



    def __str__(self):
        return self.title


class File(models.Model):
    file = models.FileField(null=True, blank=True, upload_to='uploads')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE,
                                 related_name='files')


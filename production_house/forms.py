from django import forms
from django.forms import formset_factory
from accounts.models import Teacher
from .models import Batch, Course, File, Resource

class ResourceCreateForm(forms.ModelForm):
  file = forms.FileField(
          required=False,
          widget=forms.ClearableFileInput(attrs={'name': 'file', 'multiple': True})
     )
  class Meta:
        model = Resource
        fields = ['course', 'session', 'batches', 'title', 'content', 'file']


class UploadedFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file']


UploadedFileFormSet = formset_factory(UploadedFileForm, extra=1)
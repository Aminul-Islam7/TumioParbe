from django import forms
from accounts.models import Teacher
from .models import Batch, Course, Resource

class ResourceCreateForm(forms.ModelForm):
  course = forms.ModelChoiceField(queryset=Course.objects.all())

  def __init__(self, *args, **kwargs):
    self.request = kwargs.pop("request")
    super(ResourceCreateForm, self).__init__(*args, **kwargs)
    if self.request.user.is_admin:
      self.fields['course'].queryset = Course.objects.all()
    elif self.instance.user.is_teacher:
      self.fields['course'].queryset = Course.objects.filter(id__in=Teacher.objects.filter(user_id=self.request.user.id))


  class Meta:
        model = Resource
        fields = ['course', 'session', 'batches', 'title', 'content']
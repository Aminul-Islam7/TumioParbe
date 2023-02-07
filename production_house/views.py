from urllib import response
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ResourceCreateForm
from .models import Course, Resource, Session, Batch


# Create your views here.


def dashboard(request):
    return render(request, 'production_house/dashboard.html')


class CourseList(UserPassesTestMixin, ListView):
    model = Course
    template_name = 'production_house/courses.html'
    context_object_name = 'courses'

    def test_func(self):
        return self.request.user.is_admin


class CourseCreate(UserPassesTestMixin, CreateView):
    model = Course
    fields = ['title']
    template_name = 'production_house/course_create.html'
    success_url = reverse_lazy('courses')

    def test_func(self):
        return self.request.user.is_admin


class CourseUpdate(UserPassesTestMixin, UpdateView):
    model = Course
    fields = ['title']
    template_name = 'production_house/course_update.html'
    # context_object_name = 'courses'
    success_url = reverse_lazy('courses')
    
    def test_func(self):
        return self.request.user.is_admin


class CourseDelete(UserPassesTestMixin, DeleteView):
    model = Course
    template_name = 'production_house/course_delete.html'
    success_url = reverse_lazy('courses')

    def post(self, request, *args, **kwargs):
        if Session.objects.filter(course_id=kwargs['pk']).count() > 0:
            return render(request, 'production_house/course_nodelete.html')
        return self.delete(request, *args, **kwargs)
        
    def test_func(self):
        return self.request.user.is_admin


class SessionCreate(UserPassesTestMixin, CreateView):
    model = Session
    fields = ['title']
    template_name = 'production_house/session_create.html'
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        form.instance.course = Course.objects.get(id=self.kwargs['course_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(id=self.kwargs['course_id'])
        return context

    def test_func(self):
        return self.request.user.is_admin


class SessionUpdate(UserPassesTestMixin, UpdateView):
    model = Session
    fields = ['title']
    template_name = 'production_house/session_update.html'
    context_object_name = 'session'
    success_url = reverse_lazy('courses')
    
    def test_func(self):
        return self.request.user.is_admin


class SessionDelete(UserPassesTestMixin, DeleteView):
    model = Session
    template_name = 'production_house/session_delete.html'
    success_url = reverse_lazy('courses')

    def post(self, request, *args, **kwargs):
        if Batch.objects.filter(session_id=kwargs['pk']).count() > 0:
            return render(request, 'production_house/session_nodelete.html')
        return self.delete(request, *args, **kwargs)
        
    def test_func(self):
        return self.request.user.is_admin


class BatchCreate(UserPassesTestMixin, CreateView):
    model = Batch
    fields = ['title']
    template_name = 'production_house/batch_create.html'
    success_url = reverse_lazy('courses')

    def form_valid(self, form):
        form.instance.course = Course.objects.get(id=self.kwargs['course_id'])
        form.instance.session = Session.objects.get(
            id=self.kwargs['session_id'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Course.objects.get(id=self.kwargs['course_id'])
        context['session'] = Session.objects.get(id=self.kwargs['session_id'])
        return context
        
    def test_func(self):
        return self.request.user.is_admin


class BatchUpdate(UserPassesTestMixin, UpdateView):
    model = Batch
    fields = ['title']
    template_name = 'production_house/batch_update.html'
    context_object_name = 'batch'
    success_url = reverse_lazy('courses')
    
    def test_func(self):
        return self.request.user.is_admin


class BatchDelete(UserPassesTestMixin, DeleteView):
    model = Batch
    template_name = 'production_house/batch_delete.html'
    success_url = reverse_lazy('courses')
    
    def test_func(self):
        return self.request.user.is_admin


class ResourceList(ListView):
    model = Resource
    template_name = 'production_house/resources.html'
    context_object_name = 'resources'
    ordering = ['-posted_on']
    

class ResourceDetail(DetailView):
    model = Resource
    template_name = 'production_house/resource_detail.html'
    context_object_name = 'resource'


class ResourceCreate(CreateView):
    model = Resource
    form_class = ResourceCreateForm
    template_name = 'production_house/resource_create.html'
    # success_url = reverse_lazy('resources')
    # fields = ['title', 'content', 'course', 'session', 'batches']
    
    def get_success_url(self):

        if 'post' in self.request.POST:
            return reverse('resources')

        elif 'attach-file' in self.request.POST:
            return reverse('courses')

        
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ResourceUpdate(UpdateView):
    model = Resource
    fields = ['title']
    template_name = 'production_house/resource_update.html'
    # context_object_name = 'Resources'
    success_url = reverse_lazy('resources')


class ResourceDelete(DeleteView):
    model = Resource
    template_name = 'production_house/resource_delete.html'
    success_url = reverse_lazy('resources')

    def post(self, request, *args, **kwargs):
        if Session.objects.filter(Resource_id=kwargs['pk']).count() > 0:
            return render(request, 'production_house/resource_nodelete.html')
        return self.delete(request, *args, **kwargs)

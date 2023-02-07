from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('courses/', views.CourseList.as_view(), name='courses'),
    path('new-course/',
         views.CourseCreate.as_view(), name='course-create'),
    path('edit-course/<int:pk>/',
         views.CourseUpdate.as_view(), name='course-update'),
    path('delete-course/<int:pk>/',
         views.CourseDelete.as_view(), name='course-delete'),
    path('course/<int:course_id>/add-session/',
         views.SessionCreate.as_view(), name='session-create'),
    path('edit-session/<int:pk>/',
         views.SessionUpdate.as_view(), name='session-update'),
    path('delete-session/<int:pk>/',
         views.SessionDelete.as_view(), name='session-delete'),
    path('course/<int:course_id>/session/<int:session_id>/add-batch',
         views.BatchCreate.as_view(), name='batch-create'),
    path('edit-batch/<int:pk>/',
         views.BatchUpdate.as_view(), name='batch-update'),
    path('delete-batch/<int:pk>/',
         views.BatchDelete.as_view(), name='batch-delete'),

    path('resources/', views.ResourceList.as_view(), name='resources'),
    path('resource/<int:pk>/', views.ResourceDetail.as_view(), name='resource-detail'),
    path('post-resource/', views.ResourceCreate.as_view(), name='resource-create'),
]

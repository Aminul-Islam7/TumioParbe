from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/abritti/', views.course1, name='course1'),
    path('courses/spoken-english/', views.course2, name='course2'),
    path('awards/', views.awards, name='awards'),
]

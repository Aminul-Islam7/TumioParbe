from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from .forms import LoginForm
from .views import register, register_teacher, profile, edit_profile, sign_out

urlpatterns = [
    path('register/', register, name='register'),
    path('TeacherRegister/', register_teacher, name='teacher-register'),
    path('login/', views.LoginView.as_view(template_name="accounts/login.html",
         authentication_form=LoginForm), name='login'),
    path('logout/', sign_out, name='logout'),
    path('change-password/', views.PasswordChangeView.as_view(template_name='accounts/password_change.html'),
         name='password_change'),
    path('password-changed/', views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),
         name='password_change_done'),
    path('reset-password/', views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset-done/', views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('confirm-password-reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('profile/', profile, name='profile'),
    path('edit-profile/', edit_profile, name='edit-profile'),
]

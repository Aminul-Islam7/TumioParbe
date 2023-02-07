from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from .forms import AdminUpdateForm, StudentUpdateForm, TeacherUpdateForm, UserRegisterForm, StudentRegisterForm, TeacherRegisterForm, UserUpdateForm, AuthenticationForm

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        student_form = StudentRegisterForm(request.POST,
                                           request.FILES)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            profile = student_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(
                request, 'Your account has been created! You can login and join courses now.')
            return redirect('login')

    else:
        user_form = UserRegisterForm()
        student_form = StudentRegisterForm()

    context = {
        'user_form': user_form,
        'student_form': student_form
    }

    return render(request, 'accounts/student-register.html', context)


def register_teacher(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        teacher_form = TeacherRegisterForm(request.POST,
                                           request.FILES)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save(commit=False)
            user.is_student = False
            user.is_teacher = True
            user.save()
            profile = teacher_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(
                request, f'Your account has been created!')
            return redirect('login')

    else:
        user_form = UserRegisterForm()
        teacher_form = TeacherRegisterForm()

    context = {
        'user_form': user_form,
        'teacher_form': teacher_form,
    }

    return render(request, 'accounts/teacher-register.html', context)


@login_required
def profile(request):

    # context = {
    #     ''
    # }
    return render(request, 'accounts/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)

        if request.user.is_student:
            profile_form = StudentUpdateForm(
                request.POST,
                request.FILES,
                instance=request.user.student)
        elif request.user.is_teacher:
            profile_form = TeacherUpdateForm(
                request.POST,
                request.FILES,
                instance=request.user.teacher)
        else:
            profile_form = AdminUpdateForm(
                request.POST,
                request.FILES,
                instance=request.user.admin)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'Your accont has been updated!')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        if request.user.is_student:
            profile_form = StudentUpdateForm(instance=request.user.student)
        elif request.user.is_teacher:
            profile_form = TeacherUpdateForm(instance=request.user.teacher)
        else:
            profile_form = AdminUpdateForm(instance=request.user.admin)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'accounts/profile_edit.html', context)


def sign_out(request):
    logout(request)
    return redirect('home')

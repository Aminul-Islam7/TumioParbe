from datetime import datetime
from dateutil.relativedelta import relativedelta
from django import forms
from .models import Student, Teacher, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import Div
from crispy_bootstrap5.bootstrap5 import FloatingField
from django_countries.fields import CountryField


def check_num(value):
    if not (value.isdigit() and value[0] == '0' and value[1] == '1'):
        raise forms.ValidationError('Invalid number')
    return value


def older_than20(value):
    today = datetime.now().date()
    age = relativedelta(today, value).years
    if age >= 20:
        raise forms.ValidationError(
            "You must be younger than 20 years to register.")
    return value


def younger_than2(value):
    today = datetime.now().date()
    age = relativedelta(today, value).years
    if age < 2:
        raise forms.ValidationError(
            "You must be older than 2 years.")
    return value


class UserRegisterForm(UserCreationForm):

    password1 = forms.CharField(
        label='Password*',
        widget=forms.PasswordInput(),
        help_text="Enter a strong and uncommon password with at least 8 characters."
    )
    password2 = forms.CharField(
        label='Confirm Password*',
        widget=forms.PasswordInput(),
        help_text="Enter the same password as before, for verification."
    )
    phone = forms.CharField(
        label='Phone*',
        help_text="Enter 11-digit number",
        min_length=11,
        max_length=11,
        validators=[check_num],
    )

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'phone',
            'first_name',
            'last_name',
        ]
        labels = {
            'username': 'Username*',
            'password1': 'Password*',
            'password2': 'Confirm Password*',
            'email': 'Email*',
            'first_name': 'First Name*',
            'last_name': 'Last Name*',
        }
        help_texts = {
            'username': 'No spaces. Use letters, digits, and these (@ + . _ -) characters only.'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                "Account Info:",
                Div(FloatingField('username')),
                css_class='row',
            ),
            Div(
                Div(FloatingField('password1'), css_class="col-sm-6"),
                Div(FloatingField('password2'), css_class="col-sm-6"),
                css_class='row',
            ),
            Div(
                Div(FloatingField('email'), css_class="col-sm-6"),
                Div(FloatingField('phone'), css_class="col-sm-6"),
                css_class='row',
            ),
            Fieldset(
                "Personal Info:",
                Div(FloatingField('first_name'), css_class="col-sm-6"),
                Div(FloatingField('last_name'), css_class="col-sm-6"),
                css_class='row',
            ),
        )


class TeacherRegisterForm(forms.ModelForm):
    image = forms.ImageField(
        label='Profile Picture',
        help_text='Upload a recent clear image.',
        required=False,
    )
    birth_date = forms.DateField(
        label='Birth Date',
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
    )
    facebook = forms.URLField(
        label='Facebook Profile URL',
        required=False,
    )

    class Meta:
        model = Teacher
        fields = [
            'image',
            'birth_date',
            'facebook',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div('image', css_class="col-sm-6"),
                Div('birth_date', css_class="col-sm-6"),
                css_class='row',
            ),
            FloatingField('facebook'),
        )


class StudentRegisterForm(forms.ModelForm):
    # Personal
    image = forms.ImageField(
        label='Profile Picture',
        help_text='Upload a recent clear image.',
        required=False,
    )
    birth_date = forms.DateField(
        label='Birth Date',
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        help_text='Your age must be between 2 and 20 years.',
        validators=[younger_than2, older_than20],
    )
    school = forms.CharField(
        label='School / Institute',
        required=False,
        max_length=255,
    )
    grade = forms.CharField(
        label='Class / Grade',
        required=False,
        max_length=10,
    )
    facebook = forms.URLField(
        label='Facebook Profile Link',
        required=False,
        help_text="Student or parent's facebook profile URL."
    )

    # Parents'
    father_name = forms.CharField(
        label="Father's Name",
        required=False,
        max_length=50,
    )
    mother_name = forms.CharField(
        label="Mother's Name",
        required=False,
        max_length=50,
    )
    father_phone = forms.CharField(
        label="Father's Phone",
        help_text="Enter 11-digit number",
        min_length=11,
        max_length=11,
        validators=[check_num],
        required=False,
    )
    mother_phone = forms.CharField(
        label="Mother's Phone",
        help_text="Enter 11-digit number",
        min_length=11,
        max_length=11,
        validators=[check_num],
        required=False,
    )

    # Address
    country = CountryField(default='BD').formfield()
    state = forms.CharField(
        label="Division / State",
        required=False,
        max_length=50,
    )
    city = forms.CharField(
        label="District",
        help_text="District, city, town or village",
        required=False,
        max_length=50,
    )
    area = forms.CharField(
        label="Area",
        help_text="Area, road or street name",
        required=False,
    )
    road = forms.CharField(
        label="Street / Road No.",
        required=False,
        max_length=5,
    )
    house = forms.CharField(
        label="House",
        required=False,
        max_length=50,
    )
    flat = forms.CharField(
        label="Apartment / Flat",
        required=False,
        max_length=50,
    )
    zip = forms.CharField(
        label="Zip / Postal Code",
        required=False,
        max_length=9,
    )

    class Meta:
        model = Student
        fields = [
            # Personal
            'image',
            'birth_date',
            'school',
            'grade',
            'facebook',
            # Parents'
            'father_name',
            'mother_name',
            'father_phone',
            'mother_phone',
            # Address
            'country',
            'state',
            'city',
            'area',
            'road',
            'house',
            'flat',
            'zip',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div('image', css_class="col-sm-6"),
                Div('birth_date', css_class="col-sm-6"),
                css_class='row',
            ),
            Div(
                Div(FloatingField('school'), css_class="col-sm-6"),
                Div(FloatingField('grade'), css_class="col-sm-6"),
                css_class='row',
            ),
            FloatingField('facebook'),
            Fieldset(
                "Parents' Info:",
                Div(FloatingField('father_name'), css_class="col-sm-6"),
                Div(FloatingField('mother_name'), css_class="col-sm-6"),
                css_class='row',
            ),
            Div(
                Div(FloatingField('father_phone'), css_class="col-sm-6"),
                Div(FloatingField('mother_phone'), css_class="col-sm-6"),
                css_class='row',
            ),
            Fieldset(
                "Address:",
                Div(FloatingField('country'), css_class="col-sm-6"),
                Div(FloatingField('state'), css_class="col-sm-6"),
                css_class='row',
            ),
            Div(
                Div(FloatingField('city'), css_class="col-sm-6"),
                Div(FloatingField('area'), css_class="col-sm-6"),
                css_class='row',
            ),
            Div(
                Div(FloatingField('road'), css_class="col-sm-6"),
                Div(FloatingField('house'), css_class="col-sm-6"),
                css_class='row',
            ),
            Div(
                Div(FloatingField('flat'), css_class="col-sm-6"),
                Div(FloatingField('zip'), css_class="col-sm-6"),
                css_class='row',
            ),
        )


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label='Username / Email / Phone',
    )
    error_messages = {
        "invalid_login": (
            "Please enter a correct Username / Email / Phone and Password. Both fields are case-sensitive."
        ),
    }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Div(FloatingField('username'), css_class="col-12"),
                Div(FloatingField('password'), css_class="col-12"),
                css_class='row',
            )
        )


class UserUpdateForm(forms.ModelForm):
    username = UsernameField(
        help_text=""
    )
    phone = forms.CharField(
        min_length=11,
        max_length=11,
        validators=[check_num],
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'phone',
            'first_name',
            'last_name',
        ]
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                "Account Info:",
                Div(FloatingField('username')),
                css_class='row',
            ),
            Div(
                Div(FloatingField('email'), css_class="col-sm-6"),
                Div(FloatingField('phone'), css_class="col-sm-6"),
                css_class='row',
            ),
            Fieldset(
                "Personal Info:",
                Div(FloatingField('first_name'), css_class="col-sm-6"),
                Div(FloatingField('last_name'), css_class="col-sm-6"),
                css_class='row',
            ),
        )


class StudentUpdateForm(forms.ModelForm):
    # Personal
    image = forms.ImageField(
        label='Profile Picture',
    )
    birth_date = forms.DateField(
        label='Birth Date',
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
        validators=[younger_than2],
    )
    school = forms.CharField(
        label='School / Institute',
        required=False,
        max_length=255,
    )
    grade = forms.CharField(
        label='Class / Grade',
        required=False,
        max_length=10,
    )
    facebook = forms.URLField(
        label='Facebook Profile Link',
        required=False,
    )

    # Parents'
    father_name = forms.CharField(
        label="Father's Name",
        required=False,
        max_length=50,
    )
    mother_name = forms.CharField(
        label="Mother's Name",
        required=False,
        max_length=50,
    )
    father_phone = forms.CharField(
        label="Father's Phone",
        min_length=11,
        max_length=11,
        validators=[check_num],
        required=False,
    )
    mother_phone = forms.CharField(
        label="Mother's Phone",
        min_length=11,
        max_length=11,
        validators=[check_num],
        required=False,
    )

    # Address
    country = CountryField(default='BD').formfield()
    state = forms.CharField(
        label="Division / State",
        required=False,
        max_length=50,
    )
    city = forms.CharField(
        label="District",
        required=False,
        max_length=50,
    )
    area = forms.CharField(
        label="Area",
        required=False,
    )
    road = forms.CharField(
        label="Street / Road No.",
        required=False,
        max_length=5,
    )
    house = forms.CharField(
        label="House",
        required=False,
        max_length=50,
    )
    flat = forms.CharField(
        label="Apartment / Flat",
        required=False,
        max_length=50,
    )
    zip = forms.CharField(
        label="Zip / Postal Code",
        required=False,
        max_length=9,
    )

    class Meta:
        model = Student
        fields = [
            # Personal
            'image',
            'birth_date',
            'school',
            'grade',
            'facebook',
            # Parents'
            'father_name',
            'mother_name',
            'father_phone',
            'mother_phone',
            # Address
            'country',
            'state',
            'city',
            'area',
            'road',
            'house',
            'flat',
            'zip',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'image',
            'birth_date',
            Div(
                Div(FloatingField('school'), css_class="col-sm-6"),
                Div(FloatingField('grade'), css_class="col-sm-6"),
                css_class='row',
            ),
            FloatingField('facebook'),
            Fieldset(
                "Parents' Info:",
                Div(FloatingField('father_name'), css_class="col-sm-6"),
                Div(FloatingField('mother_name'), css_class="col-sm-6"),
                css_class='row',
            ),
            Div(
                Div(FloatingField('father_phone'), css_class="col-sm-6"),
                Div(FloatingField('mother_phone'), css_class="col-sm-6"),
                css_class='row',
            ),
            Fieldset(
                "Address:",
                Div(FloatingField('country'), css_class="col-sm-6"),
                Div(FloatingField('state'), css_class="col-sm-6"),
                css_class='row',
            ),
            Div(
                Div(FloatingField('city'), css_class="col-sm-6"),
                Div(FloatingField('area'), css_class="col-sm-6"),
                css_class='row',
            ),
            Div(
                Div(FloatingField('road'), css_class="col-sm-6"),
                Div(FloatingField('house'), css_class="col-sm-6"),
                css_class='row',
            ),
            Div(
                Div(FloatingField('flat'), css_class="col-sm-6"),
                Div(FloatingField('zip'), css_class="col-sm-6"),
                css_class='row',
            ),
        )


class TeacherUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        label='Profile Picture',
    )
    birth_date = forms.DateField(
        label='Birth Date',
        widget=forms.widgets.DateInput(attrs={'type': 'date'}),
    )
    facebook = forms.URLField(
        label='Facebook Profile URL',
        required=False,
    )

    class Meta:
        model = Teacher
        fields = [
            'image',
            'birth_date',
            'facebook',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'image',
            'birth_date',
            FloatingField('facebook'),
        )


class AdminUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        label='Profile Picture',
    )

    class Meta:
        model = Teacher
        fields = [
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            'image',
        )

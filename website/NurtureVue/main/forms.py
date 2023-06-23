from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, AbstractUser
from django.core.exceptions import ValidationError
from django.forms import HiddenInput

from .models import *



class AddNewGreenhouse(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(AddNewGreenhouse, self).__init__(*args, **kwargs)
        self.fields['profile'].widget = HiddenInput()
        self.fields['profile'].required = False
        self.fields['latitude'].widget = HiddenInput()
        self.fields['longitude'].widget = HiddenInput()
        self.fields['latitude'].required = False
        self.fields['longitude'].required = False

    def clean(self):
        cleaned_data = super().clean()
        latitude = cleaned_data.get('latitude')
        longitude = cleaned_data.get('longitude')

        if not latitude or not longitude:
            raise forms.ValidationError('Please select a location on the map.')

    class Meta:
        model = greenhouse
        fields = '__all__'
        widgets = {
            'location': forms.TextInput(attrs={'placeholder': 'location'}),
            'imei': forms.TextInput(attrs={'placeholder': 'imei'}),
        }
        labels = {
            'location':'Enter the location of the greenhouse',
            'imei':'Enter the imei of your chip',
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Enter your name', widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password','id':'passwordInput'}))
    password2 = forms.CharField(label='Again enter password', widget=forms.PasswordInput(attrs={'placeholder': 'Again enter password','id':'passwordInput2'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(RegisterUserForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile.objects.create(
                user=user,
                name='None',
                surname='None',
                number_phone='None',
                city='None'
            )
        return user
class ChangPr(forms.ModelForm):

    name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    surname = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    number_phone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Номер телефона'}))
    city = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Город'}))

    class Meta:
        model = User
        fields = ('name', 'surname', 'number_phone', 'city')

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(RegisterUserForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            profile = Profile.objects.create(
                user=user,
                name=self.cleaned_data['name'],
                surname=self.cleaned_data['surname'],
                number_phone=self.cleaned_data['number_phone'],
                city=self.cleaned_data['city']
            )
        return user
"""class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password','id':'passwordInput'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password','id':'passwordInput2'}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {
            'username': forms.TextInput()
        }
"""


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password','id':'passwordInput'}))

"""class AddPostForm(forms.ModelForm):
    your_imei = forms.CharField(label='Your name', max_lenght=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title"""


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Почту',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите Почту',
            'autocomplete': 'off'
        })
    )
    username = forms.CharField(
        label='Введите Логин',
        required=True,
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите Логин',
            'autocomplete': 'off'
        })
    )
    password1 = forms.CharField(
        label='Введите Пароль',
        required=True,
        help_text='Пароль не долже быть маленьким и простым',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите Пароль',
            'autocomplete': 'off'
        })
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Подтвердите пароль',
            'autocomplete': 'off'
        })
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label='Имя пользователя',
        required=False,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы: @/./+/-/_.',
        widget=forms.TextInput(attrs={
            'class': 'form-control help-text',
            'placeholder': 'Введите Логин'
        })
    )
    email = forms.EmailField(
        label='Email',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите Почту'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Изображение профиля',
        required=True
    )

    class Meta:
        model = Profile
        fields = ['img']


class UpdateGenderSelection(forms.ModelForm):
    selections = (
        (' ', '-'),
        ('m', 'Мужской пол.'),
        ('w', 'Женский пол.')
    )
    gender = forms.ChoiceField(
        choices=selections,
        label='Выберите пол',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ['gender']


class MailAgreement(forms.ModelForm):
    agreement = forms.BooleanField(
        label='Соглашение про отправку уведомлений на почту',
        label_suffix='',
        required=False,
        widget=forms.CheckboxInput()
    )

    class Meta:
        model = Profile
        fields = ['agreement']

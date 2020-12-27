from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileImageForm, UserUpdateForm, UpdateGenderSelection, MailAgreement
from django.contrib import messages # создаем успешные или неуспешные сообщения
from django.contrib.auth.decorators import login_required # Декаратор


def register(request):
    if request.method == "POST": # Данные передачи формы регистрации
        form = UserRegisterForm(request.POST) # POST - это все данные полученные из формы
        if form.is_valid(): # проверит корректны ли данные
            form.save()
            username = form.cleaned_data.get('username') # получаем логин зарегистрируемого пользователя
            messages.success(request, f'Пользователь {username} был успешно создан') # выводит сообщение
            return redirect('home') # передресовывает после успешной регистрации на главную страницу
    else:
        form = UserRegisterForm()

    data = {
        'title': 'Страница регистрации',
        'form': form
    }
    return render(request, 'users/registration.html', context=data)


@login_required # проверяет на авторизация
def profile(request):
    if request.method == "POST":
        profileForm = ProfileImageForm(request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)
        genderSelection = UpdateGenderSelection(request.POST, instance=request.user.profile)
        mailAgreement = MailAgreement(request.POST, instance=request.user.profile)
        if profileForm.is_valid() and updateUserForm.is_valid() and genderSelection.is_valid():
            updateUserForm.save()
            profileForm.save()
            genderSelection.save()
            mailAgreement.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен!')  # выводит сообщение
            return redirect('profile')  # передресовывает после успешного обновления на ту же страницу
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        genderSelection = UpdateGenderSelection(instance=request.user.profile)
        mailAgreement = MailAgreement(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)
    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
        'genderSelection': genderSelection,
        'mailAgreement': mailAgreement

    }

    return render(request, 'users/profile.html', context=data)
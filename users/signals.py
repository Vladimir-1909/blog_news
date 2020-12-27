from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save # отслеживает сохранение в БД
from django.dispatch import receiver # обработчик действия


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # sender-табличка. instance-обьект который регестрируеться. created-состояние этой регистрации.
    # sender-с каторой моделью работаем, instance-тот обьет который был создан,
    # created-как было создано, **rwargs-дополнительные аргументы

    # если пользователь был создан, в таком случае мы обращаемя к табличке Profile,
    # функции create() создать новый обьет в определенной табличке(Profile),
    # в поле user мы устанавливаем тот обьект, который регистрировался
    # устанавливаем ссылку на обьект в табличке User
    if created:
        Profile.objects.create(user=instance)



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): # instance = user (зарегистрированный пользователь)
    # Обновление пользователя
    instance.profile.save()

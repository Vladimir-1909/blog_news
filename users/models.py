from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Автор', on_delete=models.CASCADE) # ссылка на другую запись
    img = models.ImageField('Изображение профиля', default='default.png', upload_to='user_images')

    selections = (
        (' ', '-'),
        ('m', 'Мужской пол.'),
        ('w', 'Женский пол.')
    )
    gender = models.CharField('Выберите пол', max_length=1, choices=selections, default='')

    agreement = models.BooleanField('Соглашение на уведомление', default=False)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'


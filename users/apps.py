from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # подключение сигналов
    def ready(self):
        import users.signals

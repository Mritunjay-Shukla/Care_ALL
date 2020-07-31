from django.apps import AppConfig


class UseraccountConfig(AppConfig):
    name = 'useraccount'

    def ready(self):
        import useraccount.signals
from django.apps import AppConfig


class StaticUnderscoreI18NConfig(AppConfig):
    name = 'staticunderscorei18n'

    def ready(self):
        from . import conf  # noqa

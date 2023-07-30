from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'



    # proyekti run edende siganl'i cagirmaq lazimdir apps.py'da, ki islesin
    def ready(self):
        import base.signals

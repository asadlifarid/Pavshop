from django.apps import AppConfig


class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'

    # proyekti run edende siganl'i cagirmaq lazimdir apps.py'da, ki islesin
    def ready(self):
        import blogs.signals
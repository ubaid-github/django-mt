from django.apps import AppConfig
# from django.db.models.signals import post_migrate

class MyAppConfig(AppConfig):  # Make sure the class name matches your app's config class
    name = 'app'  # Replace 'app' with your actual app name
    default_auto_field = 'django.db.models.BigAutoField'

    
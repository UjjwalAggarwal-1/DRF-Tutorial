from django.dispatch import receiver
from django.core.signals import request_finished, request_started, got_request_exception

@receiver(request_started)
def my_callback(sender, environ, **kwargs):
    print(environ)
    print("Request finished!")

from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from example.models import LoggedInUser


@receiver(user_logged_in)
def on_user_login(sender, **kwargs):
	LoggedInUser.objects.get_or_create(usuario = kwargs.get('user'))


@receiver(user_logged_out)
def on_user_logout(sender, **kwargs):
	LoggedInUser.objects.filter(usuario=kwargs.get('user')).delete()
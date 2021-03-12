from django.db import models
from django.conf import settings

class LoggedInUser(models.Model):
	usuario = models.OneToOneField(
		settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
		related_name='logged_in_user'
		)
from django.apps import AppConfig


class ChannelxConfig(AppConfig):
    name = 'ChannelX'


    def ready(self):
    	import ChannelX.signals
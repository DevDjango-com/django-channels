from channels.routing import route
from ChannelX.consumers import ws_connect, ws_disconnect

from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

application = ProtocolTypeRouter({ 

	'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    #url(r"chat/", ChatConsumer, name='chat')
                    url(r"connect/$", ws_connect, name='chat'),
                    url(r"disconnect/$", ws_disconnect, name='chat')
                ]
            )
        ),
    ),

})
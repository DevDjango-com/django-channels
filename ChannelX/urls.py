
from django.urls import path

from .views import lista_usuarios, log_in, log_out, registro

urlpatterns = [
	
    path('log_in/', log_in, name='log_in'),
    path('log_out/', log_out, name='log_out'),
    path('registro/', registro, name='registro'),
    path('', lista_usuarios, name='lista_usuarios')

]
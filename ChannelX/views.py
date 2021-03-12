from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse

User = get_user_model()

@login_required(login_url='/log_in/')
def lista_usuarios(request):

	"""
	NOTA: este es para fines de de mostracion, este codigo
	deberia ser refactorizado cuando realizemos el deploy 
	en producion. Imaginate tener 100.000 usuarios loggeados entrar y salir de nuestra aplicación afectaría el rendimiento de este código!

	"""

	usuarios = User.object.select_related('logged_in_user')
	for usuario in usuarios:
		usuario.status = 'Online' if hasattr(usuario, 'logged_in_user') else 'Offline'

	return render(request, 'lista_usuarios.html', {'usuario':usuarios})


def log_in(request):
	form = AuthenticationForm()
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
			return redirect(reverse('lista_usuarios'))
		else:
			print(form.errors)
	return render(request, 'log_in.html', {'form':form})


@login_required(login_url='/log_in/')
def log_out(request):
	logout(request)
	return redirect(reverse('log_in'))


def registro(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect(reverse('log_in'))
		else:
			print(form.errors)

	return render(request, 'registro.html', {'form':form})
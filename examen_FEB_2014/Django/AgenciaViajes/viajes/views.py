from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import View
from django.views.generic import TemplateView

#Destinos

def verDestino (request):
	dest = Destino.objects.all()
	context = {'destinos':dest}
	return render(request, 'verDestino.html', context)

def detalleDestino (request, destino_id):
	dest = Destino.objects.get(pk=destino_id)
	context = {'destinoDetalle':dest}
	return render(request, 'detalleDestino.html', context)

def addDestino(request):
	if request.method == 'POST' :
		dest = Destino()
		formulario = DestinoForm (request.POST, instance = dest)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else :
		formulario = DestinoForm()
	return render_to_response ('addDestino.html', {'formulario':formulario}, context_instance = RequestContext(request))


#Viajes

def verViajes (request):
	via = Viaje.objects.all()
	context = {'viajes':via}
	return render(request, 'verViajes.html', context)


def addViaje(request):
	if request.method == 'POST' :
		via = Viaje()
		formulario = ViajeForm (request.POST, instance = via)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/')
	else :
		formulario = ViajeForm()
	return render_to_response ('addViaje.html', {'formulario':formulario}, context_instance = RequestContext(request))


def detalleViaje (request, viaje_id):
	via = Viaje.objects.get(pk=viaje_id)
	context={'viajeDetalle':via}
	return render(request,'detalleViaje.html',context)


def editarViaje(request, viaje_id):
	viaje = get_object_or_404(Viaje, pk = viaje_id)
	if request.method == 'POST':
		formulario = ViajeForm(request.POST, instance = viaje)
 
		if formulario.is_valid():
			formulario.save()
           	return HttpResponseRedirect('/')
	else:
 
		formulario = ViajeForm(instance = viaje)
        context = { 'formulario': formulario,}
	return render_to_response('editarViaje.html', context,  context_instance=RequestContext(request))



#Usuarios

def userLogin(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            user = request.POST['username']
            passwd = request.POST['password']
            access = authenticate(username=user, password=passwd)
            if access is not None:
                if access.is_active:
                    login(request, access)
                    return redirect('/')
                else:
                    return render(request, 'inactive.html')
            else:
                return render(request, 'nouser.html')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request,'login.html', context)


@login_required(login_url='/login')
def userLogout(request):
    logout(request)
    return redirect('/')



#Rutas (con Vistas basadas en clases)

class verRuta(View):
    template_name = 'verRuta.html'
    def get(self, request, *args, **kwargs):
        rutas = Ruta.objects.all()
        return render(request, self.template_name, {'rutas':rutas})


class addRuta(View):
    form_class = RutaForm
    template_name = 'addRuta.html'

    def get(self, request, *args, **kwargs):
        formulario = self.form_class()        
        return render(request, self.template_name, {'formulario': formulario})

    def post(self, request, *args, **kwargs):
        formulario = self.form_class(request.POST, request.FILES)
        if formulario.is_valid():    
            formulario.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'formulario': formulario})


class detalleRuta(View):
    template_name = 'detalleRuta.html'

    def get(self, request, *arg, **kwargs):
        id = self.kwargs['Ruta_id']
        ruta = get_object_or_404(Ruta, pk = id)     
        return render(request,self.template_name,{'rutaDetalle':ruta,'user':request.user})



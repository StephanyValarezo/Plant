from django.shortcuts import render
from django.http import HttpResponse
from PlantApp.models import Botones
from PlantApp.forms import FormularioEstado

# Create your views here.

def botones (request):

    if request.method=="POST":
        
        miFormulario=FormularioEstado(request.POST)
        

        if miFormulario.is_valid():
            
            infForm=miFormulario.cleaned_data
            
            
            art=Botones.objects.filter(id=1).update(nombre='boton1',estado=infForm['estado'])
          
            articulos2=Botones.objects.get(id=1)
            
            return render(request, "home.html",{"articulos2":articulos2,"form":miFormulario})

    else:

        miFormulario=FormularioEstado()
        

    return render(request, "home.html", {"form":miFormulario})


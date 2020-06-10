from django.shortcuts import render
from django.http import HttpResponse
from PlantApp.models import Botones
from api_basic.models import Article
from PlantApp.forms import FormularioEstado

# Create your views here.

def botones (request):

    if request.method=="POST":
        
        miFormulario=FormularioEstado(request.POST)
        

        if miFormulario.is_valid():
            
            infForm=miFormulario.cleaned_data
            
            
            art=Article.objects.filter(id=2).update(title='boton1',estado=infForm['estado'])
          
            articulos2=Article.objects.get(id=2)
            
            return render(request, "home.html",{"articulos2":articulos2,"form":miFormulario})

    else:

        miFormulario=FormularioEstado()
        

    return render(request, "home.html", {"form":miFormulario})


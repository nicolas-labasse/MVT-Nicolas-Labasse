from django.shortcuts import render

from MVTPrimerProyectoApp.models import Persona

# Create your views here.

def documento(request):

  documento =  Persona.objects.all()
  contexto = {'documentos': documento}

  


  return render(request,"MVTPrimerProyectoApp/index.html",contexto)
from django.shortcuts import render

from MVTPrimerProyectoApp.models import Persona

# Create your views here.

def documento(request):

  documento =  Persona.objects.all()

  


  return render(request,"MVTPrimerProyectoApp/index.html",{'documentos': documento})



def nosotros(request):

  documento =  Persona.objects.all()

  
  return render(request,"MVTPrimerProyectoApp/nosotros.html",{'documentos': documento})

def escuela(request):

  documento =  Persona.objects.all()

  
  return render(request,"MVTPrimerProyectoApp/escuela.html",{'documentos': documento})
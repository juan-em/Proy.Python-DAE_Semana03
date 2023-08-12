from django.shortcuts import render
from .models import Pregunta, Opcion
# Create your views here.

def index(request):
    pregunta = Pregunta.objects.all #select * from encuesta_pregunta
    print(pregunta)
    context = {
        'lista_preguntas': pregunta
    }
    return render(request, 'encuesta/index.html', context)


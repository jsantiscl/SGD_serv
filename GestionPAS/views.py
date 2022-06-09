from django.shortcuts import render

# Create your views here.
def pas_inicio(request):

    #Aca en icontains pongo el filtro con el metodo icontains que es un like
    context = {}
    return render(request, 'GestionPAS/pas_inicio.html', context)

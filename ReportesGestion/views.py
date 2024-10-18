from django.shortcuts import render

# Create your views here.
def reportejd(request):
    reportes = [
        {
            "id": 1,
            "titulo": "Formulario de Consultas",
            "imagen_url": "url_imagen1",
            "kpi_url": "url_kpi1",
            "mini_kpi_url": "https://app.powerbi.com/view?r=eyJrIjoiY2ViN2IyYjMtOTRlNC00ZWZmLTllOTMtZjc4NWEyZjk4MjNmIiwidCI6IjI0ODMxZWJlLWQyNmQtNGQzMC05ZmE4LWVmM2MwMjQzYjMyZSIsImMiOjR9",
            "reporte_url": "https://app.powerbi.com/view?r=eyJrIjoiY2RhMDA2MGEtZGY2MS00OGUyLWEzZjctYzM5MjU3YjMwMzQ2IiwidCI6IjI0ODMxZWJlLWQyNmQtNGQzMC05ZmE4LWVmM2MwMjQzYjMyZSIsImMiOjR9"
        },
        {
            "id": 2,
            "titulo": "Aportes Electorales",
            "imagen_url": "url_imagen1",
            "kpi_url": "url_kpi1",
            "mini_kpi_url": "https://app.powerbi.com/view?r=eyJrIjoiNzA0YzljOTEtNmZhNS00MDNkLWI2MDYtOGE5MGFlYjA5OWQyIiwidCI6IjI0ODMxZWJlLWQyNmQtNGQzMC05ZmE4LWVmM2MwMjQzYjMyZSIsImMiOjR9",
            "reporte_url": "https://app.powerbi.com/view?r=eyJrIjoiMjZjYTI1ZjctYzNjNC00Mjg5LWI5MjUtZDEyMjUwNDA4NWVhIiwidCI6IjI0ODMxZWJlLWQyNmQtNGQzMC05ZmE4LWVmM2MwMjQzYjMyZSIsImMiOjR9"
        },
        # Otros reportes...
    ]
    return render(request,'ReportesGestion/reportejd.html' , {'reportes': reportes})

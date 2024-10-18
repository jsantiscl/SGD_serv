from django.urls import path
from . import views

urlpatterns = [
    path('reportejd/', views.reportejd, name='reportejd'),

]

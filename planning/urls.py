"""planning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('EditEleve/<int:id>/', views.editEleve, name='EditEleve'),
    path('ajout/', views.ajout, name='ajout'),
    path('liste/', views.liste, name='liste'),
    path('delE/<int:id>/', views.delEleve, name='dele'),
    path('index/', views.Index, name='index'),
    path('add_planning/', views.addPlanning, name='add'),
    path('del/<int:id>/', views.delPlanning, name='del'),
    path('edit/<int:id>/', views.editPlanning, name='edit'),
    path('presabs/', views.presence_absence, name='presabs'),
    path('cahierTexe/', views.cahier_texte, name='cahierTexte'),
    path('notification/', views.notifications, name='notification'),

]

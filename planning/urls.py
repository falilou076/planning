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
from django.conf.urls import url
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_user, name='login'),
    path('home/', views.home_prof, name='home'),
    path('homeSe/', views.home_secretaire, name='homeSec'),

    path('plaquetteProf/', views.IndexPlaquetteProf, name='plaquetteProf'),
    path('plaquetteSec/', views.IndexPlaquetteSec, name='plaquetteSec'),



    path('deconnexion/',views.deconnexion, name='deconnexion' ),
    path('listeEleveProf/',views.liste_eleve_prof, name='listeEleveProf' ),
    path('listeEleveSecret/',views. liste_eleve_secretaire, name='liste_eleve_secretaire' ),



    path('EditEleve/<int:id>/', views.editEleve, name='EditEleve'),
    path('ajout/', views.ajout, name='ajout'),
    path('liste_eleve/', views.liste_eleve, name='liste_eleve'),
    path('delE/<int:id>/', views.delEleve, name='dele'),
    path('index/', views.Index, name='index'),
    path('index_eleve/', views.Index_eleve, name='index_eleve'),
    path('add_planning/', views.addPlanning, name='add'),
    path('del/<int:id>/', views.delPlanning, name='del'),
    path('edit/<int:id>/', views.editPlanning, name='edit'),
    path('notification/<int:id>/', views.notifications, name='notification'),
    path('addPlaquette/', views.AjoutPlaquette, name='addPlaquette'),
    path('addPlaquette1/', views.AjoutPlaquette1, name='addPlaquette1'),
    path('addPlaquette2/', views.AjoutPlaquette2, name='addPlaquette2'),
    path('addPlaquette3/', views.AjoutPlaquette3, name='addPlaquette3'),
    path('addPlaquette4/', views.AjoutPlaquette4, name='addPlaquette4'),
    path('editPlaquette/<int:id>/', views.editPlaquette, name='editPlaquette'),
    path('editPlaquette1/<int:id>/', views.editPlaquette1, name='editPlaquette1'),
    path('editPlaquette2/<int:id>/', views.editPlaquette2, name='editPlaquette2'),
    path('editPlaquette3/<int:id>/', views.editPlaquette3, name='editPlaquette3'),
    path('editPlaquette4/<int:id>/', views.editPlaquette4, name='editPlaquette4'),
    path('DelPlaquette/<int:id>/', views.DelPlaquette, name='delplaquette'),
    path('DelPlaquette1/<int:id>/', views.DelPlaquette1, name='delplaquette1'),
    path('DelPlaquette2/<int:id>/', views.DelPlaquette2, name='delplaquette2'),
    path('DelPlaquette3/<int:id>/', views.DelPlaquette3, name='delplaquette3'),
    path('DelPlaquette4/<int:id>/', views.DelPlaquette4, name='delplaquette4'),

    path('classe/', views.classe, name='classe'),

]
admin.site.site_header = " Administrateur"
admin.site.site_title = "Planning"
admin.site.index_title = "Welcome to Planning Project Admin"
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name = 'Index' ),
    path('auth/', views.auth, name = 'Auth' ),
    path('links/', views.links, name = 'Links' ),
    path('reg/', views.reg, name = 'Reg' ),
    
]
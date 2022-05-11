"""metalpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('usuario/', include('apps.users.api.urls')),
    path('cliente/', include('apps.clients.api.urls')),
    path('proveedor/', include('apps.providers.api.urls')),
    path('maquinaria/', include('apps.machines.api.urls')),
    path('material/', include('apps.materials.api.urls')),
    path('produccion/', include('apps.productions.api.urls')),
    path('orden/', include('apps.orders.api.urls')),
    path('mantenimiento/', include('apps.mantenimiento.api.urls')),
    path('tratamiento/', include('apps.tratamiento.api.urls')),
    path('insumo/', include('apps.insumos.api.urls')),
    path('piezas/',include('apps.piezas.api.urls')),
    path('planos/',include('apps.planos.api.urls')),
    path('variables/', include('apps.variables.api.urls')),
    path('instrumentos/', include('apps.instrumentos.api.urls'))
]

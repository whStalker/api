from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from med_card import views

diagnos = DefaultRouter()
diagnos.register(r"diagnos", views.DiagnoseViewSet, basename="diagnos")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(diagnos.urls)),
    path('login/', obtain_auth_token, name="api_token")
]

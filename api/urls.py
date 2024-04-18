from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from med_card import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', views.HelloView.as_view(), name='hello'),
    path('login/', obtain_auth_token, name="api_token")
]

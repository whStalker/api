from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from med_card import views

router = DefaultRouter()
# router.register(r"diagnos", views.DiagnoseViewSet, basename="diagnos"),
router.register(r"users", views.PatientViewSet, basename="user")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path('login/', views.AuthUser.as_view(), name="api_token"),
    path('diagnos/', views.DiagnoseViewSet.as_view({'get': 'list'}), name="all-diagnos"),
    path('diagnos/create/', views.DiagnoseViewSet.as_view({'post': 'create'}), name='diagnos-create'),
    path('me/', views.UserDetailView.as_view(), name="about-user"),
]

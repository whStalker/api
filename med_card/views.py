from datetime import datetime

from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework import filters
from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import DiagnosSerializer, MedUserSerializer
from .models import Diagnos, MedUser, MedRole, User


class AuthUser(ObtainAuthToken):
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        username, password = request.data.get("username"), request.data.get("password")

        user = get_user_model().objects.filter(
            username=username
        ).first()
        med_user = MedUser.objects.filter(
            username=username
        ).first()


        if (user and user.check_password(password)) or (med_user and med_user.check_password(password)):
            if med_user:
                token, _ = Token.objects.get_or_create(user=med_user)
                med_user.last_login = datetime.now()
                med_user.save()
            else:
                token, _ = Token.objects.get_or_create(user=user)
                user.last_login = datetime.now()
                user.save()

            return Response({'token': token.key})
        else:
            msg = 'Unable to log in with provided credentials.'
            raise serializers.ValidationError(msg, code='authorization')


class DiagnoseViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Diagnos.objects.all()
    serializer_class = DiagnosSerializer

    def create(self, request):
        serializer = DiagnosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class PatientViewSet(viewsets.ModelViewSet):
    queryset = MedUser.objects.filter(role=MedRole.PATIENT)
    serializer_class = MedUserSerializer
    search_fields = ["first_name", "last_name", "username"]
    filter_backends = [filters.SearchFilter]


class UserDetailView(generics.RetrieveAPIView):
    queryset = MedUser.objects.all()
    serializer_class = MedUserSerializer
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=MedUser.objects.filter(user_ptr=request.user.id).first())
        return Response(serializer.data)

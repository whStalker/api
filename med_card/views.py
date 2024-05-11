from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import LoginSerializer, DiagnosSerializer, MedUserSerializer
from .models import Diagnos, MedUser, MedRole


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
    # queryset = MedUser.objects.all()
    serializer_class = MedUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

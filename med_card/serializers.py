from rest_framework import serializers
from django.contrib.auth import authenticate, login
from rest_framework.response import Response

from .models import Diagnos

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username'),
        password = attrs.get('password'),

        user = authenticate(self.context['request'], username=attrs.get('username'), password=attrs.get('password'))

        if not user:
            return Response({"message": 'Wrong credentials'})

        self.validated_data['user'] = user
        return attrs


class DiagnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnos
        fields = "__all__"

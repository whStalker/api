from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.response import Response
from med_card.models import Diagnos, MedUser


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


class MedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedUser
        fields = "__all__"


class DiagnosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnos
        fields = "__all__"

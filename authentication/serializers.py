from .models import Owner
from django.db import transaction
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    phone_number = serializers.CharField(max_length=30)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.phone_number = self.data.get('phone_number')
        user.save()
        return user


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = (
            'pk',
            'email',
            'username',
            'phone_number',
        )
        read_only_fields = ('pk', 'email', 'phone_number',)

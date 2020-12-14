from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mail_processed.models import Emails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups','emails']

# class EmailPredictedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Emails
#         fields = ['subject','content','user','predicted']

from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class EmailPredictedSerializer(serializers.Serializer):
    # subject = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=1500)
    user = serializers.ReadOnlyField(source='user.username')
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    predicted = serializers.IntegerField(read_only=True)
    created = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Emails` instance, given the validated data.
        """
        # TODO acá deberiamos asignar el resultado de la función de predicción.
        validated_data['predicted'] = 0
        return Emails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Emails` instance, given the validated data.
        """
        # instance.subject = validated_data.get('subject', instance.subject)
        instance.text = validated_data.get('text', instance.content)
        instance.user = validated_data.get('user', instance.user)
        instance.predicted = validated_data.get('predicted', instance.predicted)
        instance.save()
        return instance




# ANALIZAR ESTE CÓDIGO A VER SI SIRVE PARA EL TEMA DEL TOKEN
""" from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest.apps.user.models import User


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password is not found.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }


 """


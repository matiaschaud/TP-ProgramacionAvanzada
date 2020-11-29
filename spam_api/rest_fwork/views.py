from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from mail_processed.models import Emails
from .serializers import UserSerializer, EmailPredictedSerializer,UserSerializer
from rest_framework import mixins
from rest_framework import generics
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Para los permisos
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class EmailsPredictedViewSet(viewsets.ModelViewSet):
#     queryset = Emails.objects.all()
#     serializer_class = EmailPredictedSerializer
#     permission_classes = [permissions.IsAuthenticated]
    

class EmailsList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Emails.objects.all()
    serializer_class = EmailPredictedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            resp = self.create(request, *args, **kwargs)
            predicted = resp.data['predicted']
            if predicted == 1:
                predicted = 'SPAM'
            else:
                predicted = 'HAM'

            return Response({'result': predicted, 'status': 'ok'})
        
        except:
            return Response({'not_implemented'})

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmailsDetail(APIView):
    """
    Retrieve, update or delete a emails instance.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                            IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return Emails.objects.get(pk=pk)
        except Emails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        emails = self.get_object(pk)
        serializer = EmailPredictedSerializer(emails)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        emails = self.get_object(pk)
        serializer = EmailPredictedSerializer(emails, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        emails = self.get_object(pk)
        emails.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
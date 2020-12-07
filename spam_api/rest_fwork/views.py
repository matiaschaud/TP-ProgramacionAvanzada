from django.shortcuts import render, redirect

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
from rest_framework import authentication
# from .permissions import IsOwnerOrReadOnly


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
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

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
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

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


from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token


class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('emails-list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)
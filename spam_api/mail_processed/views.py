from django.shortcuts import render
from .models import Emails
from django.contrib.auth.models import User
from django.http import HttpResponse



# Create your views here.


def probando_emails(request):
    emails = Emails.objects.all()
    print(request.user.token)


    return HttpResponse(emails)
    
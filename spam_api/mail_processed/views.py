from django.shortcuts import render
from .models import Emails
from django.contrib.auth.models import User
from django.http import HttpResponse



# Create your views here.


def probando_emails(request):
    emails = Emails.objects.all()
            
    # for email in Emails.objects.get(user=request.user):
    #     print(email.user.email)
    print(Emails.objects.filter(user=request.user))
    # if request.method == "POST":
    #     data = request.GET
    #     return HttpResponse(data)
    return HttpResponse(emails)
    
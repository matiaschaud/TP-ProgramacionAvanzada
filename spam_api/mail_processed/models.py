from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Emails(models.Model):
    subject   = models.CharField(verbose_name="Asunto", max_length=200)
    content   = models.CharField(verbose_name="Contenido",max_length=1500)
    user      = models.ForeignKey('auth.User', related_name='emails', on_delete=models.CASCADE)
    created   = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de petición")
    predicted = models.IntegerField(verbose_name="Predicción spam/ham",null=True)

    class Meta:
        verbose_name = "email"
        verbose_name_plural = "emails"

    def __str__(self):
        return self.subject


# podemos hacer esto para guardar info extra calculada de los campos del mail. Es como un trigger.
""" @receiver(post_save, sender=Emails)
def predice_spam(sender, instance, **kwargs):
    email = Emails.objects.get(pk=instance.id)
    if email.predicted is None:
        email.predicted = 10
        email.save()
 """

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Emails(models.Model):
    # subject   = models.CharField(verbose_name="Asunto", max_length=200)
    text   = models.CharField(verbose_name="Contenido",max_length=1500)
    user      = models.ForeignKey('auth.User', related_name='emails', on_delete=models.CASCADE)
    created   = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de petición")
    predicted = models.IntegerField(verbose_name="Predicción spam/ham",null=True)

    class Meta:
        verbose_name = "email"
        verbose_name_plural = "emails"

    def __str__(self):
        return self.user.username + ' - ' + self.text


class UserExtends(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE,related_name='cuota')
	cuota = models.IntegerField(default=20)

    # class Meta:
    #     verbose_name = "cuota"
    #     verbose_name_plural = "cuotas"

    # def __str__(self):
    #     return self.usuario

# podemos hacer esto para guardar info extra calculada de los campos del mail. Es como un trigger.
@receiver(post_save, sender=User)
def predice_spam(sender, instance, **kwargs):
    # para asegurarnos que se ejecute solo la primera vez, vemos un parametro del kwargs que nos indica esto.
    if kwargs.get('created', False):
        UserExtends.objects.get_or_create(usuario=instance)


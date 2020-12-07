from django.contrib import admin

# Register your models here.
from .models import Emails
from .models import UserExtends

# Register your models here.
class EmailsAdmin(admin.ModelAdmin):
    readonly_fields = ('created','predicted')

admin.site.register(Emails, EmailsAdmin)

class UserExtendsAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserExtends, UserExtendsAdmin)
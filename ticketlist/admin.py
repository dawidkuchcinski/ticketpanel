from django.contrib import admin
from ticketlist.models import Ticket,Status,Damage,Devicemodel,Device,Devicedamage

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Status)
admin.site.register(Damage)
admin.site.register(Device)
admin.site.register(Devicedamage)
admin.site.register(Devicemodel)

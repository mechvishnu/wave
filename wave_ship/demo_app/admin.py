from django.contrib import admin
from demo_app.models import Port,Vessel,Principal,Ticket

# Register your models here.
admin.site.register(Port)
admin.site.register(Vessel)
admin.site.register(Ticket)
admin.site.register(Principal)

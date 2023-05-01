from django.contrib import admin

from .models import *

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    list_display= ['city', 'airport', 'airport', 'code', 'country']
    


admin.site.register(Place,PlaceAdmin)

admin.site.register(Week)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(User)
admin.site.register(Ticket)
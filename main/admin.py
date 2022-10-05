from django.contrib import admin
from .models import Oil, Spares, Autochemistry, Users


admin.site.register(Oil)
admin.site.register(Spares)
admin.site.register(Autochemistry)
admin.site.register(Users)

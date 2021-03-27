from django.contrib import admin
from .models import Bills, Veg

# register Bills model from impacts
admin.site.register(Bills)

# register Veg model from impacts
admin.site.register(Veg)

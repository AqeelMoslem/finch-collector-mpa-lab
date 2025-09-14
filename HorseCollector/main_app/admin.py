from django.contrib import admin
from .models import Horse, Feeding, Toy

admin.site.register(Horse)

# Register the new Feeding model
admin.site.register(Feeding)

admin.site.register(Toy)
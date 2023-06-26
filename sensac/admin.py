from django.contrib import admin

from .models import Contacto, Newsletter, Produto, Servicos, Subscriber

# Register your models here.
admin.site.register(Produto)
admin.site.register(Contacto)
admin.site.register(Newsletter)
admin.site.register(Subscriber)
admin.site.register(Servicos)

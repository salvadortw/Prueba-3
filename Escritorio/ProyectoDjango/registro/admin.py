from django.contrib import admin
from .models import ClientePotencial, ClienteVigente, CasoCliente

# Register your models here.

@admin.register(ClientePotencial)
class ClientePotencialAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'direccion', 'telefono', 'correo_electronico')
    search_fields = ('nombre_completo', 'telefono', 'correo_electronico')
    actions = ['convertir_a_vigente']

    def convertir_a_vigente(self, request, queryset):
        for cliente_potencial in queryset:
            
            ClienteVigente.objects.create(
                nombre_completo=cliente_potencial.nombre_completo,
                telefono=cliente_potencial.telefono,
                correo_electronico=cliente_potencial.correo_electronico,
                descripcion="Cliente convertido de potencial a vigente"
            )
            cliente_potencial.delete()

        self.message_user(request, "Los clientes potenciales seleccionados han sido convertidos a clientes vigentes.")

    convertir_a_vigente.short_description = "Convertir a cliente vigente"

# Registrar ClienteVigente en el admin
@admin.register(ClienteVigente)
class ClienteVigenteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'telefono', 'correo_electronico', 'descripcion')
    search_fields = ('nombre_completo', 'telefono', 'correo_electronico')

admin.site.register(CasoCliente)
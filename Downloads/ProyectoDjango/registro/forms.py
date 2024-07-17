from django import forms
from .models import ClientePotencial, ClienteVigente, CasoCliente
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm
from .models import AgenteVentas
from django.contrib.auth.models import User

class AgenteVentasLoginForm(AuthenticationForm):
    rut = forms.CharField(max_length=20)

    def clean(self):
        cleaned_data = super().clean()
        rut = cleaned_data.get('rut')
        password = cleaned_data.get('password')

        if rut and password:
            try:
                agente = AgenteVentas.objects.get(rut=rut)
                user = agente.user
                if not user.check_password(password):
                    raise forms.ValidationError("RUT o contraseña incorrectos.")
            except AgenteVentas.DoesNotExist:
                raise forms.ValidationError("RUT o contraseña incorrectos.")

        return cleaned_data

class AgenteVentasCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = AgenteVentas
        fields = ['rut', 'email', 'password']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['rut'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password']
        )
        agente = super().save(commit=False)
        agente.user = user
        if commit:
            agente.save()
        return agente

class ClientePotencialForm(forms.ModelForm):
    class Meta:
        model = ClientePotencial
        fields = ['RUT', 'nombre_completo', 'direccion', 'telefono', 'correo_electronico']

class ClienteVigenteForm(forms.ModelForm):
    class Meta:
        model = ClienteVigente
        exclude = ['descripcion']

class CasoClienteForm(forms.ModelForm):
    class Meta:
        model = CasoCliente
        fields = ['rut_cliente', 'nombre', 'descripcion_caso']

    def clean_rut_cliente(self):
        rut_cliente = self.cleaned_data['rut_cliente']
        validate_rut(rut_cliente)  # Llama a la función de validación personalizada
        return rut_cliente
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        # Realiza cualquier validación adicional necesaria para el campo 'nombre'
        return nombre

def validate_rut(value):
    try:
        cliente_potencial = ClientePotencial.objects.get(RUT=value)
    except ClientePotencial.DoesNotExist:
        cliente_potencial = None
        
    if not cliente_potencial:
        raise ValidationError('El RUT ingresado no corresponde a un cliente registrado.')
    
class QuejaForm(forms.ModelForm):
    rut_cliente = forms.CharField(label='RUT', max_length=12)
    descripcion_caso = forms.CharField(label='Queja o reclamo', widget=forms.Textarea)

    class Meta:
        model = CasoCliente
        fields = ['rut_cliente', 'descripcion_caso']

    def clean_rut_cliente(self):
        rut_cliente = self.cleaned_data['rut_cliente']

        # Verificar si el RUT existe en los clientes potenciales o vigentes
        try:
            cliente_potencial = ClientePotencial.objects.get(RUT=rut_cliente)
        except ClientePotencial.DoesNotExist:
            cliente_potencial = None
        

        if not cliente_potencial:
            raise forms.ValidationError('El RUT ingresado no corresponde a un cliente registrado en nuestro sistema.')

        return rut_cliente

    def clean(self):
        cleaned_data = super().clean()
        rut_cliente = cleaned_data.get('rut_cliente')

        if not rut_cliente:
            raise forms.ValidationError({'rut_cliente': 'Este campo es obligatorio.'})

        return cleaned_data
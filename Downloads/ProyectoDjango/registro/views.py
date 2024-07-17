from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ClientePotencialForm, ClienteVigenteForm, CasoClienteForm, QuejaForm
from .models import ClientePotencial, ClienteVigente, CasoCliente
from datetime import date, datetime, timedelta
from django.db.models import Count
from django.contrib.auth import authenticate, login
from .forms import AgenteVentasLoginForm
from django.contrib.auth.decorators import login_required
from .forms import AgenteVentasCreateForm
from .models import AgenteVentas
from .models import ClientePotencial
from .forms import ClientePotencialForm

@login_required
def crear_cliente(request):
    if request.method == 'POST':
        form = ClientePotencialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente.')
            return redirect('dashboard_agente')  # Redirigir al dashboard del agente después de crear cliente
        else:
            messages.error(request, 'Error al crear cliente. Verifique los datos ingresados.')
    else:
        form = ClientePotencialForm()
    
    return render(request, 'crear_cliente.html', {'form': form})


@login_required
def dashboard_agente(request):
    # Obtener todos los clientes potenciales
    clientes = ClientePotencial.objects.all()

    # Renderizar la plantilla con la lista de clientes y opciones CRUD
    return render(request, 'dashboard_agente.html', {'clientes': clientes})
#clientes
def lista_clientes(request):
    clientes = ClientePotencial.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def detalle_cliente(request, pk):
    cliente = get_object_or_404(ClientePotencial, pk=pk)
    return render(request, 'detalle_cliente.html', {'cliente': cliente})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClientePotencialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_agente')
    else:
        form = ClientePotencialForm()
    return render(request, 'agregar_cliente.html', {'form': form})

@login_required
def editar_cliente(request, pk):
    cliente = get_object_or_404(ClientePotencial, pk=pk)
    if request.method == 'POST':
        form = ClientePotencialForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado exitosamente.')
            return redirect('dashboard_agente')  # Redirigir al dashboard después de la acción
        else:
            messages.error(request, 'Error al actualizar el cliente. Verifique los datos ingresados.')
    else:
        form = ClientePotencialForm(instance=cliente)
    
    return render(request, 'editar_cliente.html', {'form': form, 'cliente': cliente})

@login_required
def eliminar_cliente(request, pk):
    cliente = get_object_or_404(ClientePotencial, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        messages.success(request, 'Cliente eliminado exitosamente.')
        return redirect('dashboard_agente')  # Redirigir al dashboard después de la acción
    return render(request, 'confirmar_eliminar_cliente.html', {'cliente': cliente})

#crud agente
@login_required
def lista_agentes(request):
    agentes = AgenteVentas.objects.all()
    return render(request, 'clientes/lista_agentes.html', {'agentes': agentes})

@login_required
def crear_agente(request):
    if request.method == 'POST':
        form = AgenteVentasCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agente de ventas creado exitosamente.')
            return redirect('lista_agentes')
        else:
            messages.error(request, 'Error al crear el agente de ventas. Verifique los datos ingresados.')
    else:
        form = AgenteVentasCreateForm()
    return render(request, 'clientes/crear_agente.html', {'form': form})

@login_required
def editar_agente(request, pk):
    agente = get_object_or_404(AgenteVentas, pk=pk)
    if request.method == 'POST':
        form = AgenteVentasCreateForm(request.POST, instance=agente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agente de ventas actualizado exitosamente.')
            return redirect('lista_agentes')
        else:
            messages.error(request, 'Error al actualizar el agente de ventas. Verifique los datos ingresados.')
    else:
        form = AgenteVentasCreateForm(instance=agente)
    return render(request, 'clientes/editar_agente.html', {'form': form, 'agente': agente})

@login_required
def eliminar_agente(request, pk):
    agente = get_object_or_404(AgenteVentas, pk=pk)
    if request.method == 'POST':
        agente.user.delete()
        messages.success(request, 'Agente de ventas eliminado exitosamente.')
        return redirect('lista_agentes')
    return render(request, 'clientes/eliminar_agente.html', {'agente': agente})

#login agente
def login_agente(request):
    if request.method == 'POST':
        form = AgenteVentasLoginForm(data=request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            user = authenticate(request, username=rut, password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('dashboard_agente')  # Redirigir al dashboard del agente
        # Si hay errores de validación o autenticación, mostrar el formulario nuevamente
    else:
        form = AgenteVentasLoginForm()

    return render(request, 'clientes/login.html', {'form': form})

# Vista para la página de inicio
def pagina_inicio(request):
    return render(request, 'pagina_inicio.html')

# Vista para registrar cliente potencial
def registro_cliente_potencial(request):
    if request.method == 'POST':
        form = ClientePotencialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente potencial registrado con éxito.')
            return redirect('registro_cliente_potencial')
        else:
            messages.error(request, 'Error al registrar el cliente potencial. Verifique los datos ingresados.')
    else:
        form = ClientePotencialForm()
    return render(request, 'registro_cliente_potencial.html', {'form': form})

# Vista para registrar cliente vigente
def registro_cliente_vigente(request):
    if request.method == 'POST':
        form = ClienteVigenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente vigente registrado con éxito.')
            return redirect('registro_cliente_vigente')
        else:
            messages.error(request, 'Error al registrar el cliente vigente. Verifique los datos ingresados.')
    else:
        form = ClienteVigenteForm()
    return render(request, 'registro_cliente_vigente.html', {'form': form})


# Vista para el reporte diario
def reporte_diario(request):
    hoy = date.today()
    clientes_potenciales_hoy = ClientePotencial.objects.filter(fecha_registro=hoy).count()
    #casos_hoy = CasoCliente.objects.filter(fecha_registro=hoy).count()
    return render(request, 'reporte_diario.html', {
        'clientes_potenciales_hoy': clientes_potenciales_hoy,
        #'casos_hoy': casos_hoy
    })

# CRUD para clientes potenciales
def cliente_potencial_list(request):
    if request.method == 'POST':
        form = ClientePotencialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El cliente potencial ha sido registrado exitosamente.')
            return redirect('cliente_potencial_list')  # Redirecciona a la misma página después de enviar el formulario
        else:
            messages.error(request, 'Hubo un error al registrar el cliente potencial. Por favor, inténtelo nuevamente.')
    else:
        form = ClientePotencialForm()

    return render(request, 'cliente_potencial_form.html', {'form': form})

def cliente_potencial_create(request):
    if request.method == 'POST':
        form = ClientePotencialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El cliente potencial ha sido registrado exitosamente.')
            return redirect('cliente_potencial_list')
        else:
            messages.error(request, 'Hubo un error al registrar el cliente potencial. Por favor, inténtelo nuevamente.')
    else:
        form = ClientePotencialForm()
    return render(request, 'cliente_potencial_form.html', {'form': form})

def cliente_potencial_update(request, pk):
    cliente_potencial = get_object_or_404(ClientePotencial, pk=pk)
    if request.method == 'POST':
        form = ClientePotencialForm(request.POST, instance=cliente_potencial)
        if form.is_valid():
            form.save()
            messages.success(request, 'El cliente potencial ha sido actualizado exitosamente.')
            return redirect('cliente_potencial_list')
        else:
            messages.error(request, 'Hubo un error al actualizar el cliente potencial. Por favor, inténtelo nuevamente.')
    else:
        form = ClientePotencialForm(instance=cliente_potencial)
    return render(request, 'cliente_potencial_form.html', {'form': form})

def cliente_potencial_delete(request, pk):
    cliente_potencial = get_object_or_404(ClientePotencial, pk=pk)
    if request.method == 'POST':
        cliente_potencial.delete()
        messages.success(request, 'El cliente potencial ha sido eliminado exitosamente.')
        return redirect('cliente_potencial_list')
    return render(request, 'cliente_potencial_confirm_delete.html', {'cliente_potencial': cliente_potencial})

# CRUD para clientes vigentes
def cliente_vigente_list(request):
    if request.method == 'POST':
        form = ClienteVigenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El cliente vigente ha sido registrado exitosamente.')
            return redirect('cliente_vigente_list')  # Redirecciona a la misma página después de enviar el formulario
        else:
            messages.error(request, 'Hubo un error al registrar el cliente vigente. Por favor, inténtelo nuevamente.')
    else:
        form = ClienteVigenteForm()

    return render(request, 'cliente_vigente_form.html', {'form': form})

def cliente_vigente_create(request):
    if request.method == 'POST':
        form = ClienteVigenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El cliente vigente ha sido registrado exitosamente.')
            return redirect('cliente_vigente_list')
        else:
            messages.error(request, 'Hubo un error al registrar el cliente vigente. Por favor, inténtelo nuevamente.')
    else:
        form = ClienteVigenteForm()
    return render(request, 'cliente_vigente_form.html', {'form': form})

def cliente_vigente_update(request, pk):
    cliente_vigente = get_object_or_404(ClienteVigente, pk=pk)
    if request.method == 'POST':
        form = ClienteVigenteForm(request.POST, instance=cliente_vigente)
        if form.is_valid():
            form.save()
            messages.success(request, 'El cliente vigente ha sido actualizado exitosamente.')
            return redirect('cliente_vigente_list')
        else:
            messages.error(request, 'Hubo un error al actualizar el cliente vigente. Por favor, inténtelo nuevamente.')
    else:
        form = ClienteVigenteForm(instance=cliente_vigente)
    return render(request, 'cliente_vigente_form.html', {'form': form})

def cliente_vigente_delete(request, pk):
    cliente_vigente = get_object_or_404(ClienteVigente, pk=pk)
    if request.method == 'POST':
        cliente_vigente.delete()
        messages.success(request, 'El cliente vigente ha sido eliminado exitosamente.')
        return redirect('cliente_vigente_list')
    return render(request, 'cliente_vigente_confirm_delete.html', {'cliente_vigente': cliente_vigente})


# Crear cliente vigente desde cliente potencial
def hacer_cliente_vigente(request, pk):
    cliente_potencial = get_object_or_404(ClientePotencial, pk=pk)
    ClienteVigente.objects.create(
        nombre_completo=cliente_potencial.nombre_completo,
        telefono=cliente_potencial.telefono,
        correo_electronico=cliente_potencial.correo_electronico,
        descripcion="Cliente convertido de potencial a vigente"
    )
    cliente_potencial.delete()  # Eliminar cliente potencial después de convertirlo
    messages.success(request, 'El cliente potencial ha sido convertido a cliente vigente.')
    return redirect('cliente_potencial_list')

def formulario_reclamo(request):
    if request.method == 'POST':
        form = CasoClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reclamo registrado correctamente.')
            return redirect('formulario_reclamo')
        else:
            messages.error(request, 'Error al registrar el reclamo. Verifique los datos ingresados.')
    else:
        form = CasoClienteForm()
    return render(request, 'formulario_reclamo.html', {'form': form})


def registro_caso_cliente(request):
    if request.method == 'POST':
        form = CasoClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_inicio') 
    else:
        form = CasoClienteForm()
    
    return render(request, 'registro_caso_cliente.html', {'form': form})

def registrar_queja(request):
    if request.method == 'POST':
        form = QuejaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Queja registrada exitosamente.')
            return redirect('pagina_inicio')
        else:
            messages.error(request, 'Error al registrar la queja. Verifique los datos ingresados.')
    else:
        form = QuejaForm()
    
    return render(request, 'registro_caso_cliente.html', {'form': form})


# Reporte diario
def reporte_diario(request):
    # Obtener la fecha de hoy y la fecha de mañana
    hoy = date.today()
    mañana = hoy + timedelta(days=1)

    # Contar clientes potenciales registrados hoy
    clientes_potenciales_hoy = ClientePotencial.objects.filter(
        fecha__gte=datetime.combine(hoy, datetime.min.time()),  # Desde hoy a las 00:00:00
        fecha__lt=datetime.combine(mañana, datetime.min.time())  # Hasta mañana a las 00:00:00
    ).count()

    # Contar casos (quejas o sugerencias) registrados hoy
    casos_hoy = CasoCliente.objects.filter(
        fecha__gte=datetime.combine(hoy, datetime.min.time()),  # Desde hoy a las 00:00:00
        fecha__lt=datetime.combine(mañana, datetime.min.time())  # Hasta mañana a las 00:00:00
    ).count()

    return render(request, 'reporte_diario.html', {
        'clientes_potenciales_hoy': clientes_potenciales_hoy,
        'casos_hoy': casos_hoy
    })




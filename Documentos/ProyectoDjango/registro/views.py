from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .forms import ClientePotencialForm, ClienteVigenteForm, CasoClienteForm, QuejaForm
from .models import ClientePotencial, ClienteVigente, CasoCliente
from datetime import date, datetime, timedelta
from django.db.models import Count

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




from django.shortcuts import render, redirect
from .models import Clientes
# Create your views here.

def inicio_vistaClientes(request):
    lasClientes=Clientes.objects.all

    return render(request,"gestionarClientes.html", {"misclientes":lasClientes})

def registrarCliente(request):
    id_cliente=request.POST["txtid_cliente"] 
    nombre_cliente=request.POST["txtnombre"]
    direccion_cliente=request.POST["txtdireccion"]
    correo_electronico=request.POST["txtcorreo"]
    fecha_registro=request.POST["txtfecha"]
    tipo_cliente=request.POST["txtcliente"]
    telefono_cliente=request.POST["txttelefono"]
    guardarVenta=Clientes.objects.create(id_cliente=id_cliente, nombre_cliente=nombre_cliente,direccion_cliente=direccion_cliente,correo_electronico=correo_electronico, fecha_registro=fecha_registro, tipo_cliente=tipo_cliente, telefono_cliente=telefono_cliente)
    return redirect("Clientes")

def seleccionarCliente(request,id_cliente):
    clientes=Clientes.objects.get(id_cliente=id_cliente)
    return render(request, "editarClientes.html", {"misclientes": clientes})

def editarCliente(request):
    id_cliente=request.POST["txtid_cliente"] 
    nombre_cliente=request.POST["txtnombre"]
    direccion_cliente=request.POST["txtdireccion"]
    correo_electronico=request.POST["txtcorreo"]
    fecha_registro=request.POST["txtfecha"]
    tipo_cliente=request.POST["txtcliente"]
    telefono_cliente=request.POST["txttelefono"]

    clientes=Clientes.objects.get(id_cliente=id_cliente)
    clientes.id_cliente=id_cliente
    clientes.nombre_cliente=nombre_cliente
    clientes.direccion_cliente=direccion_cliente
    clientes.correo_electronico=correo_electronico
    clientes.fecha_registro=fecha_registro
    clientes.tipo_cliente=tipo_cliente
    clientes.telefono_cliente=telefono_cliente
    clientes.save()
    return redirect("Clientes")

def borrarCliente(request, id_cliente):
    clientes=Clientes.objects.get(id_cliente=id_cliente)
    clientes.delete()

    return redirect("Clientes")
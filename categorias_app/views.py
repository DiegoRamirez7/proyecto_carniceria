from django.shortcuts import render, redirect
from .models import Categorias
# Create your views here.

def inicio_vistaCategorias(request):
    lasCategorias=Categorias.objects.all()

    return render(request,"gestionarCat.html", {"miscategorias":lasCategorias})

def registrarCat(request):
    id_categoria=request.POST["txtid_categoria"]
    nombre_categoria=request.POST["txtnombre"]
    descripcion_categoria=request.POST["txtdescripcion"]
    activo=request.POST["txtactivo"]
    id_producto=request.POST["txtid_padre"]
    guardarVenta=Categorias.objects.create(id_categoria=id_categoria,nombre_categoria=nombre_categoria ,descripcion_categoria=descripcion_categoria,activo=activo,id_producto=id_producto)
    return redirect("Categoria")

def seleccionarCat(request,id_categoria):
    categorias=Categorias.objects.get(id_categoria=id_categoria)
    return render(request, "editarCat.html", {"miscategorias": categorias})

def editarCat(request):
    id_categoria=request.POST["txtid_categoria"]
    nombre_categoria=request.POST["txtnombre"]
    descripcion_categoria=request.POST["txtdescripcion"]
    activo=request.POST["txtactivo"]
    id_producto=request.POST["txtid_padre"]
    
    categorias=Categorias.objects.get(id_categoria=id_categoria)
    categorias.id_categoria=id_categoria
    categorias.nombre_categoria=nombre_categoria
    categorias.descripcion_categoria=descripcion_categoria
    categorias.activo=activo
    categorias.id_producto=id_producto
    categorias.save()
    return redirect("Categoria")

def borrarCat(request, id_categoria):
    categorias=Categorias.objects.get(id_categoria=id_categoria)
    categorias.delete()

    return redirect("Categoria")
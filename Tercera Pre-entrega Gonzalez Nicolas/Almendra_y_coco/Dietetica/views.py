from django.shortcuts import render
from Dietetica.models import *
from .forms import *

# Create your views here.

def inicio(request):
    return render(request, "Dietetica/index.html")

def vendedores(request):
    contexto={"vendedores": Vendedores.objects.all()}
    return render(request, "Dietetica/Vendedores.html", contexto)

def clientes(request):
    contexto={"clientes": Clientes.objects.all()}
    return render(request, "Dietetica/Clientes.html", contexto)

def productos(request):
    contexto={"productos": Productos.objects.all()}
    return render(request, "Dietetica/Productos.html", contexto)

def productos_por_mayor(request):
    contexto={"productosPorMayor": ProductosPorMayor.objects.all()}
    return render(request, "Dietetica/Productos_por_mayor.html", contexto)

def clientesForm(request):
    if request.method == "POST":
        miForm= ClientesForm(request.POST)
        if miForm.is_valid():
            clientes_nombre= miForm.cleaned_data.get("nombre")
            clientes_apellido= miForm.cleaned_data.get("apellido")
            clientes_email= miForm.cleaned_data.get("email")
            clientes_DNI= miForm.cleaned_data.get("DNI")
            clientes= Clientes(nombre= clientes_nombre, apellido= clientes_apellido, email= clientes_email, DNI= clientes_DNI)
            clientes.save()

            contexto= {"clientes": Clientes.objects.all()}
            return render (request,"Dietetica/clientes.html", contexto)
            
    else:
        miForm= ClientesForm()
    return render (request, "Dietetica/clientes_form.html", {"form": miForm})

def vendedoresForm(request):
    if request.method == "POST":
        miForm= VendedoresForm(request.POST)
        if miForm.is_valid():
            vendedores_nombre= miForm.cleaned_data.get("nombre")
            vendedores_apellido= miForm.cleaned_data.get("apellido")
            vendedores_email= miForm.cleaned_data.get("email")
            vendedores_DNI= miForm.cleaned_data.get("DNI")
            vendedores= Vendedores(nombre= vendedores_nombre, apellido= vendedores_apellido, email= vendedores_email, DNI= vendedores_DNI)
            vendedores.save()

            contexto= {"vendedores": Vendedores.objects.all()}
            return render (request,"Dietetica/Vendedores.html", contexto)
            
    else:
        miForm= VendedoresForm()
    return render (request, "Dietetica/vendedores_form.html", {"form": miForm})

def productosForm(request):
    if request.method == "POST":
        miForm= ProductosForm(request.POST)
        if miForm.is_valid():
            productos_nombre= miForm.cleaned_data.get("nombre")
            productos_cantidad= miForm.cleaned_data.get("gramos")
            productos_precio= miForm.cleaned_data.get("pesos")
            productos= Productos(nombre= productos_nombre, cantidad= productos_cantidad, precio= productos_precio)
            productos.save() 

            contexto= {"productos": Productos.objects.all()}
            return render (request,"Dietetica/Productos.html", contexto)
            
    else:
        miForm= ProductosForm()
    return render (request, "Dietetica/productos_form.html", {"form": miForm})

def productos_por_mayorForm(request):
    if request.method == "POST":
        miForm= Productos_pormayorForm(request.POST)
        if miForm.is_valid():
            productos_pormayor_nombre= miForm.cleaned_data.get("nombre")
            productos_pormayor_precio= miForm.cleaned_data.get("kilos")
            productos_pormayor_cantidad= miForm.cleaned_data.get("pesos")
            productos_pormayor= ProductosPorMayor(nombre= productos_pormayor_nombre, cantidad= productos_pormayor_cantidad, precio= productos_pormayor_precio)
            productos_pormayor.save()

            contexto= {"productosPorMayor": ProductosPorMayor.objects.all()}
            return render (request,"Dietetica/Productos_por_mayor.html", contexto)
            
    else:
        miForm= Productos_pormayorForm()
    return render (request, "Dietetica/productos_por_mayor_form.html", {"form": miForm})

def buscarProductos(request):
    return render(request, "Dietetica/buscar_productos.html")


def encontrarProductos(request):
    if request.GET["buscar"]:
        patron= request.GET["buscar"]
        productos=Productos.objects.filter(nombre__icontains=patron)
        contexto= {"productos":productos}
        return render(request, "Dietetica/productos.html", contexto)
    
    contexto= {"productos":Productos.objects.all()}
    return render(request, "Dietetica/productos.html", contexto)
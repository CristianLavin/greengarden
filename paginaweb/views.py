from django.shortcuts import render, redirect
from .forms import RegistroForm
from paginaweb.models import Producto
from paginaweb.Carrito import Carrito
from django.views.decorators.csrf import csrf_protect
from paginaweb.models import Usuario

def index(request): 
    return render(request, 'index.html')

def plantas(request):
    return render(request, 'plantas.html')

def login(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def maceteros(request):
    return render(request, 'maceteros.html')

@csrf_protect
def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre_completo = form.cleaned_data['nombre_completo']
            username = form.cleaned_data['username']
            correo_electronico = form.cleaned_data['correo_electronico']
            password = form.cleaned_data['password']
            usuario = Usuario.objects.create_user(nombre_completo=nombre_completo, username=username, correo_electronico=correo_electronico, password=password)
            usuario.save()
            return redirect('confirmacion')  # Redirect to confirmation
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(username=username)
            if password == usuario.password:
                request.session['usuario_id'] = usuario.id
                return redirect('index2')  # Redirect to index2 after login
            else:
                error_message = 'Nombre de usuario o contraseña incorrectos'
                return render(request, 'login.html', {'error_message': error_message})
        except Usuario.DoesNotExist:
            error_message = 'Nombre de usuario o contraseña incorrectos'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def index2(request):
    id = request.session.get('usuario_id')
    if id is None:
        return redirect('login')  # Use the named URL 'login'
    x = Usuario.objects.get(id=id)
    return render(request, 'index2.html', {'x': x.username})

def plantas2(request):
    id = request.session.get('usuario_id')
    if id is None:
        return redirect('login')  # Use the named URL 'login'
    x = Usuario.objects.get(id=id)
    productos = Producto.objects.filter(categoria='Plantas')
    return render(request, 'plantas2.html', {'productos': productos, 'x': x.username})

def maceteros2(request):
    id = request.session.get('usuario_id')
    if id is None:
        return redirect('login')  # Use the named URL 'login'
    x = Usuario.objects.get(id=id)
    productos = Producto.objects.filter(categoria='Maceteros')
    return render(request, 'maceteros2.html', {'productos': productos, 'x': x.username})

def despacho(request):
    return render(request, 'despacho.html')

def confirmacion(request):
    return render(request, 'confirmacion.html')

def confirmacion2(request):
    return render(request, 'confirmacion2.html')

def confirmacion3(request):
    return render(request, 'confirmacion3.html')

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Carrito")

def carrito(request):
    id = request.session.get('usuario_id')
    if id is None:
        return redirect('login')  # Use the named URL 'login'
    x = Usuario.objects.get(id=id)
    return render(request, 'carrito.html', {'x': x.username})

def contador(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    
    if carrito.agregar(producto):
        request.session['contador'] = request.session.get('contador', 0) + 1
    elif carrito.limpiar():
        request.session['contador'] = 0
    else:
        if carrito.restar(producto):
            request.session['contador'] = max(request.session.get('contador', 0) - 1, 0)
    
    return redirect("Carrito")



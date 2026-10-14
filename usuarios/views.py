from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def iniciar_sesion(request):
    if request.method == "POST":
        usuario = authenticate(
            request, 
            username=request.POST.get("username"), 
            password=request.POST.get("password")
        )
        
        if usuario is not None:
            login(request, usuario)
            destino = request.GET.get("next", "/")
            return redirect(destino)
        else:
            return render(
                request, 
                "usuarios/login.html",
                {"error": "Usuario o contraseña incorrectos"}
            )

    return render(request, "usuarios/login.html")

def cerrar_sesion(request):
    logout(request)
    return redirect("login")

def registro(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Validar que las contraseñas coincidan
        if password1 != password2:
            return render(request, "usuarios/registro.html", {
                "error": "Las contraseñas no coinciden"
            })

        # Validar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            return render(request, "usuarios/registro.html", {
                "error": "El nombre de usuario ya está en uso"
            })

        # Crear el usuario de forma segura
        User.objects.create_user(username=username, email=email, password=password1)
        return redirect("/usuarios/login/")

    return render(request, "usuarios/registroiden.html" if False else "usuarios/registro.html")
import json
import re
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from users.models import Users, Rol

def register_user(request):
    if request.method != 'POST':
        return JsonResponse({"success": False, "mensaje": "Método no permitido"}, status=405)
        
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST.dict()

        if not data:
            return JsonResponse({"success": False, "mensaje": "⚠ No se recibieron datos"}, status=400)

        email = data.get('email', '').strip()
        username = data.get('username', '').strip()
        password = data.get('contrasena', '')
        
        if not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return JsonResponse({"success": False, "mensaje": "Correo inválido"}, status=400)

        if Users.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "mensaje": "El correo ya está registrado"}, status=400)
            
        if Users.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "mensaje": "El nombre de usuario ya existe"}, status=400)

        rol_obj, _ = Rol.objects.get_or_create(id=2, defaults={'name': 'Cliente'})

        hashed_password = make_password(password)

        new_user = Users.objects.create(
            names=f"{data.get('primer_nombre', '')} {data.get('segundo_nombre', '')}".strip().upper(),
            firstLastname=data.get('primer_apellido', '').upper(),
            SecondLastname=data.get('segundo_apellido', '').upper(),
            email=email,
            username=username,
            password=hashed_password,
            size=data.get('talla', ''),
            dateBirth=data.get('fecha_nacimiento')
        )

        return JsonResponse({
            "success": True, 
            "mensaje": "¡Usuario registrado exitosamente en el sistema!"
        }, status=201)

    except Exception as e:
        print("Error en registro:", e)
        return JsonResponse({"success": False, "mensaje": "Error interno del servidor"}, status=500)

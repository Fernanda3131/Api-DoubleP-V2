import json
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from users.models import Users

def login_user(request):
    if request.method != 'POST':
        return JsonResponse({"success": False, "mensaje": "Método no permitido"}, status=405)

    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST.dict()

        identifier = data.get('username')  
        password = data.get('password')

        if not identifier or not password:
            return JsonResponse({"success": False, "mensaje": "Campos obligatorios faltantes"}, status=400)

        try:
            user = Users.objects.get(email=identifier)
        except Users.DoesNotExist:
            try:
                user = Users.objects.get(username=identifier)
            except Users.DoesNotExist:
                return JsonResponse({"success": False, "mensaje": "Credenciales incorrectas"}, status=401)

        if not check_password(password, user.password):
            return JsonResponse({"success": False, "mensaje": "Credenciales incorrectas"}, status=401)

        request.session['logged'] = True
        request.session['id_user'] = user.id
        request.session['username'] = user.username

        return JsonResponse({
            "success": True,
            "mensaje": f"Bienvenido de vuelta, {user.username}.",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }, status=200)

    except Exception as e:
        print("Error crítico en login:", e)
        return JsonResponse({"success": False, "mensaje": "Error interno al procesar el ingreso"}, status=500)

def logout_user(request):
    request.session.flush()
    return JsonResponse({"success": True, "mensaje": "Sesión cerrada correctamente"}, status=200)

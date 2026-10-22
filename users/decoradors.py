from functools import wraps
from django.http import JsonResponse

def login_required_api(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('logged') or not request.session.get('id_user'):
            return JsonResponse({
                "success": False, 
                "mensaje": "Acceso denegado. Debe iniciar sesión para realizar esta acción."
            }, status=401)
            
        return view_func(request, *args, **kwargs)
    return _wrapped_view

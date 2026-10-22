import json
from django.http import JsonResponse
from publications.models import Publication, PublicationStatus
from users.models import Users
from users.decoradors import login_required_api 

@login_required_api 
def save_publication(request):
    if request.method != 'POST':
        return JsonResponse({"success": False, "mensaje": "Método no permitido"}, status=405)
        
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
        else:
            data = request.POST.dict()

        description = data.get("description")
        id_status = data.get("status")
        type_publication = data.get("type") 
        id_user_sesion = request.session.get("id_user")

        try:
            status_obj = PublicationStatus.objects.get(id=id_status)
            user_obj = Users.objects.get(id=id_user_sesion)
        except (PublicationStatus.DoesNotExist, Users.DoesNotExist):
            return JsonResponse({"success": False, "mensaje": "Estado o Usuario no válidos"}, status=400)

        new_publication = Publication.objects.create(
            description=description,
            idStatus=status_obj,
            typePublication=type_publication,
            idUser=user_obj
        )

        return JsonResponse({
            "success": True, 
            "mensaje": "¡Publicación creada exitosamente!",
            "id_publicacion": new_publication.id
        }, status=201)

    except Exception as e:
        print("Error en guardar_publicacion:", e)
        return JsonResponse({"success": False, "mensaje": "Error interno del servidor"}, status=500)

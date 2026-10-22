from django.http import JsonResponse
from publications.models import Publication, Garment
from users.decoradors import login_required_api

@login_required_api
def save_garment(request):
    if request.method != 'POST':
        return JsonResponse({"success": False, "mensaje": "Método no permitido"}, status=405)
        
    try:
        name = request.POST.get("name")
        description_garment = request.POST.get("description")
        size = request.POST.get("size")
        value = request.POST.get("value")
        id_publication = request.POST.get("publication")

        photo1 = request.FILES.get("photo")
        photo2 = request.FILES.get("photo")
        photo3 = request.FILES.get("photo")
        photo4 = request.FILES.get("photo")

        try:
            publication_obj = Publication.objects.get(id=id_publication)
        except Publication.DoesNotExist:
            return JsonResponse({"success": False, "mensaje": "La publicación asociada no existe"}, status=400)

        new_garment = Garment.objects.create(
            garment=name,
            desciption=description_garment,
            size=size,
            firstPhoto=photo1,
            secondPhoto=photo2,
            thirdPhoto=photo3,
            fourthPhoto=photo4,
            value=value,
            idPublication=publication_obj
        )

        return JsonResponse({
            "success": True, 
            "mensaje": f"Prenda '{new_garment.garment}' registrada y vinculada con éxito."
        }, status=201)

    except Exception as e:
        print("Error en guardar_prenda:", e)
        return JsonResponse({"success": False, "mensaje": "Error interno al registrar prenda"}, status=500)

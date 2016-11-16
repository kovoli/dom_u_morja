from django.shortcuts import render, get_object_or_404
from .models import House  # Импорт модели

def houses_list(request):
    houses = House.objects.all()  # Запрос на получение всех объектов
    return render(request, "houses/houses_list.html", {'houses': houses})


#def house_detail(request, house_id):  # Включает id вома
 #   house = get_object_or_404(House, id=house_id)
  #  return render(request, "houses/house_detail.html", {'house': house})
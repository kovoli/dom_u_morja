from django.contrib import admin
from .models import House


@admin.register(House)  # Декоратор связывает модель с админкой
class AdminHouse(admin.ModelAdmin):
    list_display = ["name", "price"]  # показывает поля в админке


from django.db import models


class House(models.Model):
    name = models.CharField("название", max_length=50)  # Русское название поля "название"
    price = models.IntegerField("цена")  # IntegerField принимает и хранить целые цисла
    description = models.TextField("описание")
    photo = models.ImageField("фотография", upload_to="houses/photos", default="", blank=True)  # Добавление фотографии

    class Meta:
        verbose_name = "дом"
        verbose_name_plural = "дома"
        ordering = ["name"]  # Отсортирует поле наме в админке

    def __str__(self):
        return self.name

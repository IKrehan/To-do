from django.db import models


class Task(models.Model):
    name = models.CharField("Tarefa", max_length=200)
    is_active = models.BooleanField("Está Ativa", default=True)

    def __str__(self):
        return self.name
    
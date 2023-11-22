from django.db import models

# Create your models here.


class Task(models.Model):

    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
    )

    title = models.CharField(verbose_name="Titulo", max_length=70)
    descriptions = models.TextField(verbose_name="Descripcion")
    due_data = models.DateField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="pendiente")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Tarea'
        ordering = ['status']

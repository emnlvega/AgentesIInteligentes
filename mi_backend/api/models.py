from django.db import models

class Ubicacion(models.Model):
    usuario = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.usuario} - {self.latitud}, {self.longitud}"
from django.db import models

# Create your models here.
class AUDIENCIA(models.Model):
    AUDIENCIA_id = models.AutoField(primary_key=True)
    RESUMEN = models.TextField()
from django.db import models

# Create your models here.


class SobreNosotros(models.Model):
    descripcion_titulo = models.CharField(max_length=200,null=True, blank=True)
    titulo_secundario = models.CharField(max_length=100,null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(upload_to='',null=True, blank=True)
    class Meta:

        verbose_name = 'SobreNosotros'
        verbose_name_plural = "SobreNosotros"
    def __str__(self):
        return self.titulo_secundario

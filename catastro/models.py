from django.db import models

# Create your models here.
class Contribuyente(models.Model):
    """ modelo de contribuyente """
    nombre = models.CharField(max_length=100)
    ap_paterno = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    ap_materno = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    
    M = 'MASCULINO'
    F = 'FEMENINO'
    GENERO = [
        (M, 'MASCULINO'),
        (F, 'FEMENINO')
    ]
    genero = models.CharField(
        max_length=15,
        choices=GENERO,
        default=M        
    )
    
    domicilio = models.CharField(
        max_length=250,
        blank=True,
        null=True
    )
    
    localidad = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    telefono = models.BigIntegerField(
        blank=True,
        null=True
    )
        
    expediente = models.FileField(upload_to="expedientes/", null=True, blank=True)
    
    notas_adicionales = models.CharField(
        max_length=500,
        null=True,
        blank=True
    )
    
    def __str__(self):
        """ Descripción del modelo contribuyente """
        return '{} {} {}'.format(self.nombre, self.ap_paterno, self.ap_materno)
    
    def save(self):
        """ el nombre del contribuyente lo guardamos en mayúsculas"""
        self.nombre = self.nombre.upper()
        if self.ap_paterno: # si la cadena esta llena
            self.ap_paterno = self.ap_paterno.upper()
            
        if self.ap_materno: # si la cadena esta llena
            self.ap_materno = self.ap_materno.upper()
            
        super(Contribuyente, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Contribuyentes"

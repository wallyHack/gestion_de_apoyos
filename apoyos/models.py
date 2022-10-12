
from django.db import models

# Create your models here.
class Localidad(models.Model):
    """ modelo localidad"""
    nombre = models.CharField(
        max_length=200
    )

    seccion = models.IntegerField(
        null=True, blank=True
    )

    numero_habitantes = models.IntegerField(
        null=True, blank=True
    )

    def __str__(self):
        """ Descripción del modelo localidad """
        return '{}'.format(self.nombre)

    def save(self):
        """ el nombre de la localidad lo guardamos en mayúsculas"""
        self.nombre = self.nombre.upper()
        super(Localidad, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Localidades"

class Persona(models.Model):
    """ modelo persona"""
    nombres = models.CharField(
        max_length=100,
    )

    ap_paterno = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    ap_materno = models.CharField(
        max_length=100,
        null = True,
        blank = True
    )

    #example of choices
    ACTIVISTA = 'ACTIVISTA'
    ACTIVADO = 'ACTIVADO'
    CONTRA = 'CONTRA'
    OTROS = 'OTROS'
    TIPO_CLIENTE = [
        (ACTIVISTA, 'ACTIVISTA'),
        (ACTIVADO, 'ACTIVADO'),
        (CONTRA, "CONTRA"),
        (OTROS, 'OTROS')
    ]

    tipo = models.CharField(
        max_length = 15,
        choices = TIPO_CLIENTE,
        default = ACTIVISTA
    )

    domicilio = models.CharField(
        max_length=150, 
        blank = True
    )

    ACT = 'ACTIVO'
    INA = 'INACTIVO'
    ESTADO = [
        (ACT, 'ACTIVO'),
        (INA, 'INACTIVO')
    ]

    estado = models.CharField(
        max_length = 10,
        choices = ESTADO,
        default = ACT
    )

    telefono = models.BigIntegerField(
        null = True,
        blank = True
    )

    # llaves foráneas
    # una persona pertenece/vive en una comunidad
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    # una persona puede recibir uno o muchos apoyos
    # apoyos = models.ForeignKey(Apoyos, on_delete=models.CASCADE)

    def __str__(self):
        """ Descripción del modelo persona"""
        return '{} {}'.format(self.nombres, self.ap_paterno)

    def save(self):
        """ el nombre de la persona lo guardamos en mayúsculas"""
        self.nombres = self.nombres.upper()
        # si la cadena esta llena, convertimos el contenido a mayúsculas
        if self.ap_paterno or self.ap_materno:
            self.ap_paterno = self.ap_paterno.upper()
            self.ap_materno = self.ap_materno.upper()

        super(Persona, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Personas"

class Apoyos(models.Model):
    """ modelo de apoyos"""
    # choices
    ECONOMICO = 'ECONOMICO'
    VIVIENDA = 'VIVIENDA'
    SALUD = 'SALUD'
    COMBUSTIBLE = 'COMBUSTIBLE'
    IMPLEMENTOS = 'IMPLEMENTOS'
    SEMILLAS_DE_CULTIVO = 'SEMILLAS DE CULTIVO'
    OTROS = 'OTROS'
    TIPO_DE_APOYO = [
        (ECONOMICO, 'ECONOMICO'),
        (VIVIENDA, 'VIVIENDA'),
        (SALUD, 'SALUD'),
        (COMBUSTIBLE, 'COMBUSTIBLE'),
        (IMPLEMENTOS, 'IMPLEMENTOS'),
        (SEMILLAS_DE_CULTIVO, 'SEMILLAS DE CULTIVO'),
        (OTROS, 'OTROS')
    ]

    tipo = models.CharField(
        max_length = 20,
        choices = TIPO_DE_APOYO,
        default = ECONOMICO
    )

    descripcion = models.TextField(
        max_length = 250
    )

    fecha_de_entrega = models.DateField(
        null=True, blank=True
    )

    comprobacion = models.ImageField(upload_to="apoyos/", null=True, blank=True)

    notas_adicionales = models.TextField(
        max_length = 500,
        null = True,
        blank = True
    )

    # llave foránea
    # un apoyo es entregado a una persona
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    # un apoyo es entregado por un encargado
    # encargado = models.ForeignKey(EncargadoRuta, on_delete=models.CASCADE)

    persona_que_entrego = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        """ Descripción del modelo apoyo """
        return '{} {}'.format(self.tipo, self.descripcion)

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Apoyos"

class EncargadoRuta(models.Model):
    """ modelo para el encargado de ruta"""
    nombres = models.CharField(
        max_length=100
    )

    ap_paterno = models.CharField(
        max_length=100
    )

    ap_materno = models.CharField(
        max_length=100
    )

    # choices
    HOMBRE = 'HOMBRE'
    MUJER = 'MUJER'
    TIPO_DE_SEXO = [
        (HOMBRE, 'HOMBRE'),
        (MUJER, 'MUJER')
    ]

    sexo = models.CharField(
        max_length = 10,
        choices = TIPO_DE_SEXO,
        default = HOMBRE
    )

    telefono = models.BigIntegerField(
        blank = True,
        null=True
    )

    domicilio = models.TextField(
        max_length=400,
        blank = True
    )

    email = models.EmailField(
        null = True,
        blank = True
    )

    # llaves foráneas
    # un encargado de ruta administra/controla una o muchas localidades
    comunidades = models.ManyToManyField(Localidad)

    def __str__(self):
        """ Descripción del modelo encargado de ruta """
        return '{} {}'.format(self.nombres, self.ap_paterno)

    def save(self):
        """ el nombre del encargado de ruta lo guardamos en mayúsculas"""
        self.nombres = self.nombres.upper()
        # si la cadena esta llena, convertimos el contenido a mayúsculas
        if self.ap_paterno or self.ap_materno:
            self.ap_paterno = self.ap_paterno.upper()
            self.ap_materno = self.ap_materno.upper()
        super(EncargadoRuta, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Encargados de Ruta"


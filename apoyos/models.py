
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

class Puesto(models.Model):
    """ modelo de Puesto de trabajo"""
    nombre = models.CharField(max_length=200)

    def __str__(self):
        """ descripcion del puesto"""
        return '{}'.format(self.nombre)

    def save(self):
        """ el nombre del puesto de trabajo lo guardamos en mayúsculas"""
        self.nombre = self.nombre.upper()
        super(Puesto, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Puestos"


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
        null=True,
        blank=True
    )

    # example of choices
    ACTIVISTA = 'ACTIVISTA'
    ACTIVADO = 'ACTIVADO'
    CONTRA = 'CONTRA'
    OTROS = 'OTROS'
    TIPO_PERSONA = [
        (ACTIVISTA, 'ACTIVISTA'),
        (ACTIVADO, 'ACTIVADO'),
        (CONTRA, "CONTRA"),
        (OTROS, 'OTROS')
    ]

    tipo = models.CharField(
        max_length=15,
        choices=TIPO_PERSONA,
        default=ACTIVISTA
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
        max_length=150,
        blank=True
    )

    ACT = 'ACTIVO'
    INA = 'INACTIVO'
    ESTADO = [
        (ACT, 'ACTIVO'),
        (INA, 'INACTIVO')
    ]

    estado = models.CharField(
        max_length=10,
        choices=ESTADO,
        default=ACT
    )

    telefono = models.BigIntegerField(
        null=True,
        blank=True
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
        if self.ap_paterno: # si la cadena esta llena
            self.ap_paterno = self.ap_paterno.upper()
            
        if self.ap_materno: # si la cadena esta llena
            self.ap_materno = self.ap_materno.upper()
        
        super(Persona, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Personas"


class Departamento(models.Model):
    """ modelo departamento """
    nombre = models.CharField(max_length=100)
    numero_de_empleados = models.IntegerField(
        blank=True,
        null=True
    )

    # relaciones 1 o muchos
    # un departamento tiene 1 o muchos empleados
    #empleados = models.ManyToManyField(Empleado);

    def __str__(self):
        """ descripción del modelo departamento"""
        return '{}'.format(self.nombre)

    def save(self):
        """ el nombre del departamento lo guardamos en mayúsculas"""
        self.nombre = self.nombre.upper()
        super(Departamento, self).save()


class Empleado(models.Model):
    """ modelo empleado"""
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

    domicilio = models.TextField(
        max_length=250,
        blank=True,
        null=True
    )

    telefono = models.BigIntegerField(
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

    ACT = 'ACTIVO'
    INA = 'INACTIVO'
    ESTADO = [
        (ACT, 'ACTIVO'),
        (INA, 'INACTIVO')
    ]

    status = models.CharField(
        max_length=10,
        choices=ESTADO,
        default=ACT
    )

    # relaciones
    # un empleado trabaja en un departamento
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # un empleado tiene asignado un puesto
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    
    sueldo = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True
    )

    def __str__(self):
        """ descripción de empleado"""
        return '{} {} {}'.format(self.nombre, self.ap_paterno, self.ap_materno)

    def save(self):
        """ el nombre del empleado lo guardamos en mayúsculas"""
        self.nombre = self.nombre.upper()
        if self.ap_paterno: # si la cadena esta llena
            self.ap_paterno = self.ap_paterno.upper()
            
        if self.ap_materno:
            self.ap_materno = self.ap_materno.upper()

        super(Empleado, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Empleados"


class EncargadoRuta(models.Model):
    """ modelo para el encargado de ruta"""
    nombres = models.CharField(
        max_length=100
    )

    ap_paterno = models.CharField(
        max_length=100,
        blank = True,
        null = True
    )

    ap_materno = models.CharField(
        max_length=100,
        blank = True,
        null = True
    )

    # choices
    HOMBRE = 'HOMBRE'
    MUJER = 'MUJER'
    TIPO_DE_SEXO = [
        (HOMBRE, 'HOMBRE'),
        (MUJER, 'MUJER')
    ]

    sexo = models.CharField(
        max_length=10,
        choices=TIPO_DE_SEXO,
        default=HOMBRE
    )

    telefono = models.BigIntegerField(
        blank=True,
        null=True
    )

    domicilio = models.TextField(
        max_length=400,
        blank=True
    )

    email = models.EmailField(
        null=True,
        blank=True
    )

    # llaves foráneas
    # un encargado de ruta administra/controla una o muchas localidades
    comunidades = models.ManyToManyField(Localidad)
    # un encargado de ruta dirige un departamento
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        """ Descripción del modelo encargado de ruta """
        return '{} {} {}'.format(self.nombres, self.ap_paterno, self.ap_materno)

    def save(self):
        """ el nombre del encargado de ruta lo guardamos en mayúsculas"""
        self.nombres = self.nombres.upper()
        if self.ap_paterno: # si la cadena esta llena
            self.ap_paterno = self.ap_paterno.upper()
            
        if self.ap_materno: # si la cadena esta llena
            self.ap_materno = self.ap_materno.upper()
            
        super(EncargadoRuta, self).save()

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Encargados de Ruta"
        
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
        max_length=20,
        choices=TIPO_DE_APOYO,
        default=ECONOMICO
    )

    descripcion = models.TextField(
        max_length=250
    )

    fecha_de_entrega = models.DateField(
        null=True, blank=True
    )

    comprobacion = models.ImageField(
        upload_to="apoyos/", null=True, blank=True)

    notas_adicionales = models.TextField(
        max_length=500,
        null=True,
        blank=True
    )

    # llave foránea
    # un apoyo es entregado a una persona
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    # un apoyo es entregado por un encargado
    encargado_de_ruta = models.ForeignKey(
        EncargadoRuta, on_delete=models.CASCADE)
    #persona_que_entrego = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        """ Descripción del modelo apoyo """
        return '{} {}'.format(self.tipo, self.descripcion)

    class Meta:
        """ nombre en plural(Muchos) del modelo"""
        verbose_name_plural = "Apoyos"

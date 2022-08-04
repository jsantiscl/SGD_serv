from django.db import models
# prueba github
# Create your models here.
class AnunciosMeta(models.Model):
    ad_creation_time = models.DateField(null=True, blank=True)
    semana = models.IntegerField(null=True, blank=True)
    texto = models.CharField(max_length=5000, null=True, blank=True)
    ad_creative_link_caption = models.CharField(max_length=500, null=True, blank=True)
    ad_creative_link_description = models.CharField(max_length=500, null=True, blank=True)
    ad_creative_link_title = models.CharField(max_length=500, null=True, blank=True)
    ad_delivery_start_time = models.DateField(null=True, blank=True)
    ad_delivery_stop_time = models.DateField(null=True, blank=True)
    ad_snapshot_url = models.CharField(max_length=500, null=True, blank=True)
    currency = models.CharField(max_length=50, null=True, blank=True)
    funding_entity = models.CharField(max_length=500, null=True, blank=True)
    identificado = models.CharField(max_length=50, null=True, blank=True)
    nombre_homologado = models.CharField(max_length=500, null=True, blank=True)
    inscrito = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    opcion = models.CharField(max_length=50, null=True, blank=True)
    id = models.CharField(max_length=50,primary_key=True)
    page_id = models.CharField(max_length=100, null=True, blank=True)
    page_name = models.CharField(max_length=500, null=True, blank=True)
    page_name_para_cruce = models.CharField(max_length=500, null=True, blank=True)
    publisher_platforms = models.CharField(max_length=100, null=True, blank=True)
    region_distribution = models.CharField(max_length=1500, null=True, blank=True)
    lower_bound_impressions = models.IntegerField(null=True, blank=True)
    upper_bound_impressions = models.IntegerField(null=True, blank=True)
    ad_start_date = models.DateField(null=True, blank=True)
    spend = models.CharField(max_length=500, null=True, blank=True)
    low_spend = models.IntegerField(null=True, blank=True)
    up_spend = models.IntegerField(null=True, blank=True)
    gasto_max_clp = models.IntegerField(null=True, blank=True)
    plataforma = models.CharField(max_length=500, null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    sospecha_propaganda = models.IntegerField(null=True, blank=True)
    idioma = models.CharField(max_length=50, null=True, blank=True)
    gasto_prom_clp = models.IntegerField(null=True, blank=True)
    gasto_min_clp = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.id

class UsersFiscalizacion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    habilitado = models.BooleanField(default=True)
    username = models.CharField(max_length=50, default='SIN')
    tipo = models.CharField(max_length=50, default='Abogado')
    def __str__(self):
        return self.nombre

class AlertasMeta(models.Model):
    Estados = (
        ("1_Pendiente_Asignacion", "1_Pendiente_Asignacion"),
        ("2_Asignado_Abogado", "2_Asignado_Abogado"),
        ("3_Derivado_Upas", "3_Derivado_Upas"),
        ("4_Ya_Gestionado", "4_Ya_Gestionado"),
        ("5_Archivar", "5_Archivar"),

    )
    semana = models.IntegerField(null=True, blank=True)
    nombre_homologado = models.CharField(max_length=500, null=True, blank=True)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    opcion = models.CharField(max_length=100, null=True, blank=True)
    cantidad_anuncios = models.IntegerField(null=True, blank=True)
    gasto_maximo = models.IntegerField(null=True, blank=True)
    monto_aportes = models.IntegerField(null=True, blank=True)
    monto_servicios = models.IntegerField(null=True, blank=True)
    tipo_alerta = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=100,choices=Estados, default='1_Pendiente_Asignacion')
    usuario_actual = models.ForeignKey(UsersFiscalizacion, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre_homologado


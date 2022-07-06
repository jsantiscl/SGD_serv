from django.db import models

# Create your models here.
class AnunciosFacebook(models.Model):
    ad_creation_time = models.DateTimeField(null=True, blank=True)
    texto = models.CharField(max_length=5000, null=True, blank=True)
    ad_creative_link_caption = models.CharField(max_length=500, null=True, blank=True)
    ad_creative_link_description = models.CharField(max_length=500, null=True, blank=True)
    ad_creative_link_title = models.CharField(max_length=500, null=True, blank=True)
    ad_delivery_start_time = models.DateTimeField(null=True, blank=True)
    ad_delivery_stop_time = models.DateTimeField(null=True, blank=True)
    ad_snapshot_url = models.CharField(max_length=500, null=True, blank=True)
    currency = models.CharField(max_length=50, null=True, blank=True)
    funding_entity = models.CharField(max_length=500, null=True, blank=True)
    identificado = models.CharField(max_length=50, null=True, blank=True)
    q = models.IntegerField(null=True, blank=True)
    nombre_homologado = models.CharField(max_length=500, null=True, blank=True)
    inscrito = models.CharField(max_length=50, null=True, blank=True)
    tipo = models.CharField(max_length=50, null=True, blank=True)
    opcion = models.CharField(max_length=50, null=True, blank=True)
    id = models.BigIntegerField(primary_key=True)
    page_id = models.CharField(max_length=100, null=True, blank=True)
    page_name = models.CharField(max_length=500, null=True, blank=True)
    publisher_platforms = models.CharField(max_length=100, null=True, blank=True)
    region_distribution = models.CharField(max_length=1500, null=True, blank=True)
    lower_bound_impressions = models.IntegerField(null=True, blank=True)
    upper_bound_impressions = models.IntegerField(null=True, blank=True)
    ad_start_date = models.DateTimeField(null=True, blank=True)
    spend = models.CharField(max_length=500, null=True, blank=True)
    low_spend = models.IntegerField(null=True, blank=True)
    up_spend = models.IntegerField(null=True, blank=True)
    gasto_max_clp = models.IntegerField(null=True, blank=True)
    plataforma = models.CharField(max_length=500, null=True, blank=True)
    facebook = models.CharField(max_length=50, null=True, blank=True)
    instagram = models.CharField(max_length=50, null=True, blank=True)
    sospecha_propaganda = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.id

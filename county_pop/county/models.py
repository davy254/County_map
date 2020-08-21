from django.contrib.gis.db import models


class County(models.Model):
    county_nam = models.CharField(max_length=80)
    county_cod = models.FloatField()
    shape_area = models.FloatField()
    pop = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.county_nam



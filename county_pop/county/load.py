import os
from django.contrib.gis.utils import LayerMapping
from .models import County

county_mapping = {
    'county_nam': 'COUNTY_NAM',
    'county_cod': 'COUNTY_COD',
    'shape_area': 'Shape_Area',
    'pop': 'pop',
    'geom': 'MULTIPOLYGON',
}


county_shp = os.path.abspath( os.path.join(os.path.dirname(__file__), 'data', 'county1.shp'), )

def run(verbose=True):
    lm = LayerMapping(County,county_shp, county_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)


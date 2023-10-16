import ee
import folium
from datetime import datetime

ee.Authenticate()
ee.Initialize()

florianopolis = ee.Geometry.Polygon(
    [[[-48.665390, -27.665586],
      [-48.665390, -27.623179],
      [-48.530956, -27.623179],
      [-48.530956, -27.665586]]])

start_date = '2022-01-01'
end_date = '2022-12-31'

sentinel_collection = (ee.ImageCollection('COPERNICUS/S2')
                       .filterBounds(florianopolis)
                       .filterDate(start_date, end_date))

image = sentinel_collection.first()

ndvi = image.normalizedDifference(['B8', 'B4'])

mapid = ndvi.getMapId({'min': -1, 'max': 1})
map = folium.Map(location=[-27.5885, -48.5450], zoom_start=11)
folium.TileLayer(
    tiles=mapid['tile_fetcher'].url_format,
    attr='Google Earth Engine',
    overlay=True,
    name='NDVI'
).add_to(map)

display(map)

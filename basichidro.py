import ee
import folium

ee.Authenticate()
ee.Initialize()

area_de_estudo = ee.Geometry.Rectangle([-84.6, -55.9, -32.9, 15.5])

start_date = '2022-01-01'
end_date = '2022-12-31'

colecao_imagens = ee.ImageCollection('NASA_USDA/HSL/SMAP_soil_moisture') \
                .filterBounds(area_de_estudo) \
                .filterDate(start_date, end_date)

imagem = colecao_imagens.sort('system:time_start', False).first()

smi = imagem.expression('100*(1 - (VV/VV_MAX))', {
    'VV': imagem.select('ssm'),
    'VV_MAX': 0.5
})

mapid = smi.getMapId({'min': 0, 'max': 100})
map = folium.Map(location=[0, -50], zoom_start=3)
folium.TileLayer(
    tiles=mapid['tile_fetcher'].url_format,
    attr='Google Earth Engine',
    overlay=True,
    name='SMI'
).add_to(map)

display(map)

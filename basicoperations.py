import ee

# Autenticar e inicializar o Google Earth Engine
ee.Authenticate()
ee.Initialize()

# Carregar uma imagem de exemplo
image = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318')

# Operações básicas
# 1. Visualizar uma imagem
print("Visualização da imagem:")
print(image.getInfo())
print("===================")

# 2. Aplicar operações matemáticas
print("Operações matemáticas:")
soma = image.select('B5').add(image.select('B4'))
print(soma.getInfo())
print("===================")

# 3. Filtrar por região de interesse
print("Filtragem por região de interesse:")
regiao_de_interesse = ee.Geometry.Rectangle(-122.2809, 37.1209, -122.0556, 37.2413)
image_na_regiao = image.clip(regiao_de_interesse)
print(image_na_regiao.getInfo())
print("===================")

# 4. Reduzir regiões para estatísticas
print("Redução de regiões para estatísticas:")
estatisticas = image_na_regiao.reduceRegion(reducer=ee.Reducer.mean(), geometry=regiao_de_interesse, scale=30)
print(estatisticas.getInfo())
print("===================")

# 5. Filtrar imagens por data
print("Filtragem de imagens por data:")
start_date = '2014-01-01'
end_date = '2014-12-31'
colecao_filtrada_por_data = ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA') \
                            .filterDate(start_date, end_date) \
                            .filterBounds(regiao_de_interesse)
print(colecao_filtrada_por_data.size().getInfo())
print("===================")

# 6. Aplicar uma máscara em uma imagem
print("Aplicar uma máscara em uma imagem:")
mascara = image.select('B5').gt(0.5)
imagem_com_mascara = image.updateMask(mascara)
print(imagem_com_mascara.getInfo())
print("===================")

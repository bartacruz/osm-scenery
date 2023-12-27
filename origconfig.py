import math

layers=[
    {
        'name':'golf_course',
        'terrain':'GolfCourse',
        'key':'leisure',
    },
    {
        'name':'residential',
        'terrain':'Urban',
        'landuse':False
    },
    {
        'name':'farmland',
        'terrain':'MixedCrop',
        'key':'landuse',
        'landuse':True,
    },
    {
        'name':'farmyard',
        'terrain':'SubUrban',
        'key':'landuse',
        'landuse':True,
    },
    {
        'name':'orchard',
        'terrain':'Orchard',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'vineyard',
        'terrain':'Vineyard',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'scrub',
        'terrain':'Scrub',
        'key':'natural',
    },
    {
        'name':'wetland',
        'terrain':'FloodLand',
        'key':'natural',
    },
    {
        'name':'retail',
        'terrain':'BuiltUpCover',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'pitch',
        'terrain':'GrassCover',
        'key':'leisure',
    },
    {
        'name':'quarry',
        'terrain':'Burnt',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'park',
        #'terrain':'CropWood',
        'terrain':'RainForest',
    },
    {
        'name':'nature_reserve',
        'terrain':'MixedForest',
    },
    {
        'name':'military',
        'terrain':'RainForest',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'meadow',
        'terrain':'CropGrass',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'industrial',
        'terrain':'Industrial',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'harbour',
        'terrain':'Port',
        'key':'landuse',
    },
    {
        'name':'heath',
        'terrain':'Marsh',
        'key':'natural',
    },
    {
        'name':'grass',
        'terrain':'GrassCover',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'forest',
        'terrain':'EvergreenForest',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'commercial',
        'terrain':'BuiltUpCover',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'parking',
        'terrain':'BuiltUpCover',
        'landuse':False,
        'key':'amenity'
    },
    {
        'name':'cemetery',
        'terrain':'Cemetery',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'allotments',
        'terrain':'IrrCrop',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'greenhouse_horticulture',
        'terrain':'Orchard',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'bare_rock',
        'terrain':'Rock',
        'key':'natural',
    },
    {
        'name':'railway',
        'terrain':'Railroad',
        'key':'landuse',
    },
    {
        'name':'sand',
        'terrain':'Sand',
    },
    {
        'name':'construction',
        'terrain':'Construction',
        'landuse':True,
        'key':'landuse',
    },
    {
        'name':'water',
        'terrain':'Lake',
        'line-type': 'Stream',
    },
    {
        'name':'intermittent',
        'terrain':'IntermittentLake',
        'line-type':'IntermittentStream',
    },
    {
        'name':'shingles',
        'terrain':'IntermittentStream',
        'key': 'natural',
    },
    {
        'name':'neighbourhood',
        'terrain':'Town',
        'landuse':False,
    },
#    {
#        'name':'esteros',
#        'terrain':'FloodLand',
#        'external': True,
#    },
#    {
#        'name':'matorral',
#        'terrain':'Scrub',
#        'external': True,
#    },
#    {
#        'name':'espejodeagua',
#        'terrain':'Lake',
#        'external': True,
#    },
]

download_enabled = True
osm2city_enabled  = True
def get_names():
    line_layers = [y for y in layers if y.get('line-type',False)]
    #print "layers",line_layers
    lines = [x['line-type'] for x in line_layers]
    return [x['name'] for x in layers ] + lines

def tilename(lon,lat):
    plon = 'w' if lon <  0 else 'e'
    plat = 's' if lat < 0 else 'n'
    tile = '%s%03d%s%02d' % (plon,abs(lon), plat, abs(lat))
    return tile

def box2tile(box):
    south = int(box.get('south'))
    west = int(box.get('west'))
    return tilename(west,south)

def box2dir(box):
    south = int(box.get('south'))
    west = int(box.get('west'))
    lat_mult = south/abs(south)
    lon_mult = west/abs(west)
    south_edge = int(math.ceil(abs(south)/10)*10*lat_mult)
    west_edge = int(math.ceil(abs(west)/10)*10*lon_mult)
    return tilename(west_edge,south_edge)

output_dir='/home/julio/src/scenery/auto/output'
boxes = [
#{'east': '-56.5', 'north': '-37', 'south': '-37.5', 'west': '-57.5', 'xdesc': 'Mar Azul R11'},
#{'east': '-60', 'north': '-32', 'south': '-34', 'west': '-62', 'xdesc': 'Rosario Full'},
#{'east': '-58', 'north': '-33', 'south': '-35', 'west': '-60', 'xdesc': "Areco-SP-Delta"},
#{'east': '-57', 'north': '-33', 'south': '-35', 'west': '-58', 'xdesc': 'La Plata'},
#{'east': '-57', 'north': '-35', 'south': '-37', 'west': '-58', 'xdesc': 'San Borombon'},
#{'east': '-67', 'north': '-31', 'south': '-34', 'west': '-70', 'xdesc': 'CUYO'},
#{'east': '-56', 'north': '-36', 'south': '-39', 'west': '-58', 'xdesc': 'Villa Gesell Grande'},

#{'east': '-69', 'north': '-33', 'south': '-34', 'west': '-70', 'xdesc': 'Santiago Este'},
#{'east': '-70', 'north': '-32', 'south': '-33', 'west': '-71', 'xdesc': 'Santiago Norte'},
#{'east': '-70', 'north': '-33', 'south': '-34', 'west': '-71', 'xdesc': 'Santiago SCEL'}, 
#{'east': '-71', 'north': '-32', 'south': '-33', 'west': '-72', 'xdesc': 'Valparaiso'},
#{'east': '-71', 'north': '-33', 'south': '-34', 'west': '-72', 'xdesc': 'Santiago Oeste'}, 
{'east': '-71', 'north': '-33', 'south': '-34', 'west': '-72', 'xdesc': 'Santiago Sur'},
{'east': '-68', 'north': '-31', 'south': '-32', 'west': '-69', 'xdesc': 'San Juan'},
{'east': '-69', 'north': '-31', 'south': '-32', 'west': '-70', 'xdesc': 'San Juan Oeste'},
#{'east': '-69', 'north': '-32', 'south': '-33', 'west': '-70', 'xdesc': 'Mendoza oeste'},
#{'east': '-68', 'north': '-32', 'south': '-33', 'west': '-69', 'xdesc': 'Mendoza'},
{'east': '-68', 'north': '-30', 'south': '-31', 'west': '-69', 'xdesc': 'La Rioja'},
{'east': '-68', 'north': '-33', 'south': '-34', 'west': '-69', 'xdesc': 'Mendoza Sudoeste'},
{'east': '-69', 'north': '-33', 'south': '-34', 'west': '-70', 'xdesc': 'Mendoza Sur'},
{'east': '-66', 'north': '-33', 'south': '-34', 'west': '-67', 'xdesc': 'San Luis'},
#{'east': '-67', 'north': '-32', 'south': '-33', 'west': '-68', 'xdesc': 'Mendoza Este'},
#{'east': '-67', 'north': '-33', 'south': '-34', 'west': '-68', 'xdesc': 'Mendoza SE'},
#{'east': '-70', 'north': '-30', 'south': '-40', 'west': '-80', 'xdesc': 'w80s40 Chile'},
#{'east': '-70', 'north': '-34', 'south': '-42', 'west': '-72', 'xdesc': 'Cordillera Bariloche'},
#{'east': '-69', 'north': '-36', 'south': '-38', 'west': '-70', 'xdesc': 'Catriel'},
#{'east': '-70', 'north': '-40', 'south': '-42', 'west': '-72', 'xdesc': 'Bariloche Chapelco'},
#{'east': '-70', 'north': '-38', 'south': '-40', 'west': '-72', 'xdesc': 'Bariloche Norte'},
#{'east': '-70', 'north': '-36', 'south': '-38', 'west': '-72', 'xdesc': 'Bariloche Norte'},
#{'east': '-68', 'north': '-38', 'south': '-40', 'west': '-70', 'xdesc': 'Neuquen'},
#{'east': '-69', 'north': '-34', 'south': '-36', 'west': '-70', 'xdesc': 'Malargue'},
#{'east': '-70', 'north': '-42', 'south': '-44', 'west': '-72', 'xdesc': 'Bariloche Norte'},

#{'east': '-71', 'north': '-40', 'south': '-40.5', 'west': '-71.5', 'xdesc': 'San Martin de los Andes'},
#{'east': '-60.6', 'north': '-32.94', 'south': '-32.99', 'west': '-60.7', 'xdesc': ' Rosario Norte'}, # SAAR
#{'east': '-64', 'north': '-33', 'south': '-34', 'west': '-65', 'xdesc': 'CBA - Rio 4'},
#{'east': '-62', 'north': '-32', 'south': '-33', 'west': '-63', 'xdesc': 'CBA - Marcos Juarez'},
#{'east': '-63', 'north': '-32', 'south': '-33', 'west': '-64', 'xdesc': 'CBA - Villa Maria'},
#{'east': '-64', 'north': '-32', 'south': '-33', 'west': '-65', 'xdesc': 'CBA - Rio 3'},
#{'east': '-64', 'north': '-31', 'south': '-32', 'west': '-65', 'xdesc': 'CBA - Capiitaal'},
#{'east': '-61', 'north': '-32', 'south': '-33', 'west': '-62', 'xdesc': 'Rosario Oeste'},
#{'east': '-60', 'north': '-33', 'south': '-34', 'west': '-61', 'xdesc': 'Rosario Sur'},
#{'east': '-60', 'north': '-32', 'south': '-33', 'west': '-61', 'xdesc': 'Rosario Norte'}, # SAAR
#{'east': '-59', 'north': '-34', 'south': '-35', 'west': '-60', 'xdesc': 'Delta'},
#{'east': '-59', 'north': '-33', 'south': '-34', 'west': '-60', 'xdesc': 'San Pedro'},
#{'east': '-59', 'north': '-35', 'south': '-36', 'west': '-60', 'xdesc': 'Chivilcoy'},
#{'east': '-58', 'north': '-33', 'south': '-34', 'west': '-59', 'xdesc': "Areco's"},
#{'east': '-58', 'north': '-34', 'south': '-35', 'west': '-59', 'xdesc': 'Buenos Aires'},
#{'east': '-58', 'north': '-35', 'south': '-36', 'west': '-59', 'xdesc': 'Chascomus'},
#{'east': '-58', 'north': '-36', 'south': '-37', 'west': '-59', 'xdesc': 'Rauch'},
#{'east': '-58', 'north': '-37', 'south': '-38', 'west': '-59', 'xdesc': 'Balcarce'},
#{'east': '-57', 'north': '-35', 'south': '-36', 'west': '-58', 'xdesc': 'San Borombon'},
#{'east': '-57', 'north': '-34', 'south': '-35', 'west': '-58', 'xdesc': 'La Plata'},
#{'east': '-57', 'north': '-36', 'south': '-37', 'west': '-58', 'xdesc': 'Dolores'},
#{'east': '-57', 'north': '-37', 'south': '-38', 'west': '-58', 'xdesc': 'Mar Azul'},
#{'east': '-57', 'north': '-38', 'south': '-39', 'west': '-58', 'xdesc': 'Mar Del Plata'},
#{'east': '-56', 'north': '-34', 'south': '-35', 'west': '-57', 'xdesc': 'Montevideo'},
#{'east': '-56', 'north': '-36', 'south': '-37', 'west': '-57', 'xdesc': 'Ruta 11 Atlantica'},
#{'east': '-56', 'north': '-37', 'south': '-38', 'west': '-57', 'xdesc': 'Villa Gesell'},

#{'east': '-58', 'north': '-34', 'south': '-36', 'west': '-60', 'xdesc': 'CHASCO GRANDE'},
#{'east': '-65', 'north': '-26', 'south': '-30', 'west': '-67', 'xdesc': 'Tucuman'},
#{'east': '-57', 'north': '-51', 'south': '-52.5', 'west': '-61.5', 'xdesc': 'Malvinas'},
#{'east': '-68', 'north': '-54', 'south': '-55', 'west': '-69', 'xdesc': 'Usuahia'},
#{'east': '-64', 'north': '-52', 'south': '-56.5', 'west': '-75.5', 'xdesc': 'Tierra del Fuego'},
#{'east': '87', 'north': '28', 'south': '27', 'west': '86', 'xdesc': 'Lukla'},
#{'east': '86', 'north': '28', 'south': '27', 'west': '85', 'xdesc': 'Katmandu'},


#{'east': '-56', 'north': '-36', 'south': '-39', 'west': '-58', 'xdesc': 'Costa Atlantica'},
#{'east': '-58.50', 'north': '-33.57', 'south': '-34.16', 'west': '-59.17', 'xdesc': 'Zarate Campana'},
#{'east': '-56.54', 'north': '-36.19', 'south': '-37.385', 'west': '-57.90', 'xdesc': ' Villa Gesell'},
#{'east': '-57.0133', 'north': '-37.2312', 'south': '-37.239', 'west': '-57.0411', 'xdesc': ' SAZV'},
#{'east': '-57.70', 'north': '-35.40', 'south': '-35.95', 'west': '-58.30', 'xdesc': ' Chascomus'},
#{'east': '-57.465', 'north': '-36.18', 'south': '-37.00', 'west': '-57.8', 'xdesc': ' Dolores'},
#{'east': '-58.038', 'north': '-34.642', 'south': '-35.22', 'west': '-58.345', 'xdesc': ' Quilmes'},
#{'east': '-57.960', 'north': '-34.6275', 'south': '-34.88945', 'west': '-58.36847', 'xdesc': ' Autpista BsAS -La Plata'},
#{'east': '-58.1', 'north': '-34.9', 'south': '-34.98', 'west': '-58.21', 'xdesc': ' El Peligro'},
#{'east': '-57.8', 'north': '-34.642', 'south': '-36', 'west': '-59', 'xdesc': ' SADQ-Chascomus'},
#{'east': '-58.20', 'north': '-34.10', 'south': '-34.50', 'west': '-58.60', 'xdesc': 'Sanfer'},
#{'east': '-58.25', 'north': '-34.625', 'south': '-34.75', 'west': '-58.50', 'xdesc': 'SABE mal'},
#{'east': '-58.371', 'north': '-34.448', 'south': '-34.575', 'west': '-58.479', 'xdesc': ' SABE'},
#{'east': '-58.355', 'north': '-34.405', 'south': '-34.59', 'west': '-58.704', 'xdesc': ' Pala'},
#{'east': '-58.419', 'north': '-34.485', 'south': '-34.553', 'west': '-58.602', 'xdesc': ' Pala-Nunez'},
#{'east': '-59.3', 'north': '-32', 'south': '-34', 'west': '-61.2', 'xdesc': ' Rosario'},
#{'east': '-60.5', 'north': '-32.5', 'south': '-33.1', 'west': '-61', 'xdesc': ' Rosario'},
#{'east': '-57.990833', 'north': '-34.7469', 'south': '-34.854166', 'west': '-58.11', 'xdesc': 'Punta Lara'},
]

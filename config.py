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
        'name':'island',
        'terrain':'Island',
        'key':'place',
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
        'name':'scree',
        'terrain':'Construction',
        'key':'natural',
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
        'landuse':False,
#        'key':'landuse',
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
        'name':'railway_corridor',
        'line-type': 'Railroad',
        'line-width': 10,
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
        'name':'tertiary',
        'line-type': 'Road-Tertiary',
        'line-width': 5,
    },
    {
        'name':'tertiary_shoulder',
        'line-type': 'Road-Shoulder',
        'line-width': 7,
    },
    {
        'name':'other_roads',
        'line-type': 'Road-Service',
        'line-width': 5,
    },
    {
        'name':'unpaved_roads',
        'line-type': 'Road-Unclassified',
        'line-width': 5,
    },
    {
        'name':'track',
        'line-type': 'Road-Pedestrian',
        'line-width': 3,
    },
    {
        'name':'path',
        'line-type': 'Road-Pedestrian',
        'line-width': 1.5,
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
    lines = ["%s_line" % x['name'] for x in line_layers]
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
#{'east': '-73', 'north': '-43', 'south': '-44', 'west': '-74', 'xdesc': 'Islas Chile Sur'},
#
#{'east': '-72', 'north': '-43', 'south': '-44', 'west': '-73', 'xdesc': 'Balmaceda Chile'},
#{'east': '-72', 'north': '-44', 'south': '-45', 'west': '-73', 'xdesc': 'Puerto Cisnes Chile'},
#{'east': '-72', 'north': '-45', 'south': '-46', 'west': '-73', 'xdesc': 'Puerto Aysén Chile'},
#
#{'east': '-71', 'north': '-32', 'south': '-33', 'west': '-72', 'xdesc': 'Valparaiso'},
#{'east': '-71', 'north': '-33', 'south': '-34', 'west': '-72', 'xdesc': 'Santiago Oeste'}, 
#{'east': '-71', 'north': '-38', 'south': '-39', 'west': '-72', 'xdesc': 'Pehuenia'}, 
#{'east': '-71', 'north': '-39', 'south': '-40', 'west': '-72', 'xdesc': 'Lanin'}, 
#{'east': '-71', 'north': '-40', 'south': '-41', 'west': '-72', 'xdesc': 'Nahuel Huapi - La Angostura '}, 
#{'east': '-71', 'north': '-41', 'south': '-42', 'west': '-72', 'xdesc': 'Bariloche'}, 
#{'east': '-71', 'north': '-42', 'south': '-43', 'west': '-72', 'xdesc': 'El Bolson - Esquel'}, 
#{'east': '-71', 'north': '-43', 'south': '-44', 'west': '-72', 'xdesc': 'Futaleufu'}, 
#
#{'east': '-70', 'north': '-32', 'south': '-33', 'west': '-71', 'xdesc': 'Santiago Norte'},
#{'east': '-70', 'north': '-33', 'south': '-34', 'west': '-71', 'xdesc': 'Santiago SCEL'}, 
#{'east': '-70', 'north': '-35', 'south': '-36', 'west': '-71', 'xdesc': 'Malargue Oeste'},
#{'east': '-70', 'north': '-36', 'south': '-37', 'west': '-71', 'xdesc': 'Minas'},
#{'east': '-70', 'north': '-37', 'south': '-38', 'west': '-71', 'xdesc': 'RN40 - Chos Malal'},
#{'east': '-70', 'north': '-38', 'south': '-39', 'west': '-71', 'xdesc': 'RN40 - RN22 - Zapala'}, 
#{'east': '-70', 'north': '-39', 'south': '-40', 'west': '-71', 'xdesc': 'Alumine'}, 
#{'east': '-70', 'north': '-41', 'south': '-42', 'west': '-71', 'xdesc': 'Bariloche Este'}, 
##
#{'east': '-69', 'north': '-31', 'south': '-32', 'west': '-70', 'xdesc': 'San Juan Oeste'},
#{'east': '-69', 'north': '-32', 'south': '-33', 'west': '-70', 'xdesc': 'Mendoza oeste'},
#{'east': '-69', 'north': '-33', 'south': '-34', 'west': '-70', 'xdesc': 'Tunuyan'},
#{'east': '-69', 'north': '-34', 'south': '-35', 'west': '-70', 'xdesc': 'Laguna del Diamante'},
#{'east': '-69', 'north': '-35', 'south': '-36', 'west': '-70', 'xdesc': 'Malargue'},
#{'east': '-69', 'north': '-36', 'south': '-37', 'west': '-70', 'xdesc': 'La Payunia Oeste'},
#{'east': '-69', 'north': '-37', 'south': '-38', 'west': '-70', 'xdesc': 'Pehuenches'},
#{'east': '-69', 'north': '-38', 'south': '-39', 'west': '-70', 'xdesc': 'Cutral Co'},
# 
#{'east': '-69', 'north': '-51', 'south': '-52', 'west': '-70', 'xdesc': 'RN3 - Rio Gallegos Oeste'},
#{'east': '-69', 'north': '-52', 'south': '-53', 'west': '-70', 'xdesc': 'RN3 Final - Limite Chile'},
#{'east': '-69', 'north': '-54', 'south': '-55', 'west': '-70', 'xdesc': 'Chile - Oeste de Usuahia'},
#
#{'east': '-68', 'north': '-31', 'south': '-32', 'west': '-69', 'xdesc': 'San Juan'},
#{'east': '-68', 'north': '-32', 'south': '-33', 'west': '-69', 'xdesc': 'Mendoza'},
#{'east': '-68', 'north': '-30', 'south': '-31', 'west': '-69', 'xdesc': 'La Rioja'},
#{'east': '-68', 'north': '-33', 'south': '-34', 'west': '-69', 'xdesc': 'Mendoza Sudoeste'},
#{'east': '-68', 'north': '-38', 'south': '-39', 'west': '-69', 'xdesc': 'Neuquén'},
#{'east': '-68', 'north': '-51', 'south': '-52', 'west': '-69', 'xdesc': 'Rio Gallegos'},
#{'east': '-68', 'north': '-52', 'south': '-53', 'west': '-69', 'xdesc': 'Bahia Lomas'},
#{'east': '-68', 'north': '-53', 'south': '-54', 'west': '-69', 'xdesc': 'T. del Fuego'},
#{'east': '-68', 'north': '-54', 'south': '-55', 'west': '-69', 'xdesc': 'Usuahia'},
#{'east': '-68', 'north': '-55', 'south': '-56', 'west': '-69', 'xdesc': 'Isla Hoste'},
##
#{'east': '-67', 'north': '-32', 'south': '-33', 'west': '-68', 'xdesc': 'RN7 - Mendoza Este'},
#{'east': '-67', 'north': '-33', 'south': '-34', 'west': '-68', 'xdesc': 'RN7 - Mendoza SE'},
#{'east': '-67', 'north': '-53', 'south': '-54', 'west': '-68', 'xdesc': 'Rio Grande - T. del Fuego'},
#{'east': '-67', 'north': '-54', 'south': '-55', 'west': '-68', 'xdesc': 'Ushuaia Este'},
# Desde aca
#{'east': '-66', 'north': '-33', 'south': '-34', 'west': '-67', 'xdesc': 'RN7 - San Luis'},
#
#{'east': '-65', 'north': '-33', 'south': '-34', 'west': '-66', 'xdesc': 'RN7 - Villa Mercedes'},
#
#{'east': '-64', 'north': '-31', 'south': '-32', 'west': '-65', 'xdesc': 'CBA - Capiitaal'},
{'east': '-64', 'north': '-32', 'south': '-33', 'west': '-65', 'xdesc': 'CBA - Rio 3'},
{'east': '-64', 'north': '-33', 'south': '-34', 'west': '-65', 'xdesc': 'RN7- RN8 - Rio 4'},
#
{'east': '-63', 'north': '-31', 'south': '-32', 'west': '-64', 'xdesc': 'CBA - Villa del Rosario'},
{'east': '-63', 'north': '-32', 'south': '-33', 'west': '-64', 'xdesc': 'CBA - Villa Maria'},
{'east': '-63', 'north': '-33', 'south': '-34', 'west': '-64', 'xdesc': 'CBA - Juarez Celman'},
{'east': '-63', 'north': '-34', 'south': '-35', 'west': '-64', 'xdesc': 'RN7 - Laboulaye'},
#
{'east': '-62', 'north': '-31', 'south': '-32', 'west': '-63', 'xdesc': 'CBA - Este'},
{'east': '-62', 'north': '-32', 'south': '-33', 'west': '-63', 'xdesc': 'CBA - Marcos Juarez'},
{'east': '-62', 'north': '-33', 'south': '-34', 'west': '-63', 'xdesc': 'RN7 - Rufino'},
#
{'east': '-61', 'north': '-31', 'south': '-32', 'west': '-62', 'xdesc': 'CBA - Santa Fe medio'},
{'east': '-61', 'north': '-32', 'south': '-33', 'west': '-62', 'xdesc': 'Rosario Oeste'},
{'east': '-61', 'north': '-33', 'south': '-34', 'west': '-62', 'xdesc': 'Venado Tuerto'},
#
{'east': '-60', 'north': '-30', 'south': '-31', 'west': '-61', 'xdesc': 'Santa Fe Centro'}, 
{'east': '-60', 'north': '-31', 'south': '-32', 'west': '-61', 'xdesc': 'Santa Fe - Rosario'}, 
{'east': '-60', 'north': '-32', 'south': '-33', 'west': '-61', 'xdesc': 'Rosario Norte'}, # SAAR
{'east': '-60', 'north': '-33', 'south': '-34', 'west': '-61', 'xdesc': 'Rosario Sur'},
{'east': '-60', 'north': '-34', 'south': '-35', 'west': '-61', 'xdesc': 'Chacabuco'},
{'east': '-60', 'north': '-35', 'south': '-36', 'west': '-61', 'xdesc': 'Bragado'},
{'east': '-60', 'north': '-36', 'south': '-37', 'west': '-61', 'xdesc': 'Tapalqué'},
{'east': '-60', 'north': '-37', 'south': '-38', 'west': '-61', 'xdesc': 'RN3 - Laprida'},
{'east': '-60', 'north': '-38', 'south': '-39', 'west': '-61', 'xdesc': '3 Arroyos'},
#
{'east': '-59', 'north': '-30', 'south': '-31', 'west': '-60', 'xdesc': 'Entre Rios NW'},
{'east': '-59', 'north': '-31', 'south': '-32', 'west': '-60', 'xdesc': 'Entre Rios Centro'},
{'east': '-59', 'north': '-32', 'south': '-33', 'west': '-60', 'xdesc': 'Entre Rios Sur'},
{'east': '-59', 'north': '-33', 'south': '-34', 'west': '-60', 'xdesc': 'San Pedro'},
{'east': '-59', 'north': '-34', 'south': '-35', 'west': '-60', 'xdesc': 'Areco - Lujan'},
{'east': '-59', 'north': '-35', 'south': '-36', 'west': '-60', 'xdesc': 'Lobos - Roque Perez'},
{'east': '-59', 'north': '-36', 'south': '-37', 'west': '-60', 'xdesc': 'RN3 - Las Flores - Azul'},
{'east': '-59', 'north': '-37', 'south': '-38', 'west': '-60', 'xdesc': 'Tandil'},
{'east': '-59', 'north': '-38', 'south': '-39', 'west': '-60', 'xdesc': 'Necochea'},
#
{'east': '-58', 'north': '-32', 'south': '-33', 'west': '-59', 'xdesc': "Entre Rios NE"},
{'east': '-58', 'north': '-33', 'south': '-34', 'west': '-59', 'xdesc': "Entre Rios SE - Delta"},
{'east': '-58', 'north': '-34', 'south': '-35', 'west': '-59', 'xdesc': 'Buenos Aires'},
{'east': '-58', 'north': '-35', 'south': '-36', 'west': '-59', 'xdesc': 'Gral Belgrano - Chascomus'},
{'east': '-58', 'north': '-36', 'south': '-37', 'west': '-59', 'xdesc': 'Rauch - Pila'},
{'east': '-58', 'north': '-37', 'south': '-38', 'west': '-59', 'xdesc': 'Ayacucho - Balcarce'},
{'east': '-58', 'north': '-38', 'south': '-39', 'west': '-59', 'xdesc': 'Loberia'},
#
{'east': '-57', 'north': '-34', 'south': '-35', 'west': '-58', 'xdesc': 'La Plata'},
{'east': '-57', 'north': '-35', 'south': '-36', 'west': '-58', 'xdesc': 'Magdalena - San Borombon'},
{'east': '-57', 'north': '-36', 'south': '-37', 'west': '-58', 'xdesc': 'Dolores'},
{'east': '-57', 'north': '-37', 'south': '-38', 'west': '-58', 'xdesc': 'Mar Azul - Mar Chiquita'},
{'east': '-57', 'north': '-38', 'south': '-39', 'west': '-58', 'xdesc': 'Mar Del Plata'},
#
{'east': '-56', 'north': '-34', 'south': '-35', 'west': '-57', 'xdesc': 'Montevideo'},
{'east': '-56', 'north': '-36', 'south': '-37', 'west': '-57', 'xdesc': 'Ruta 11 Atlantica'},
{'east': '-56', 'north': '-37', 'south': '-38', 'west': '-57', 'xdesc': 'Villa Gesell'},
#
{'east': '-55', 'north': '-34', 'south': '-35', 'west': '-56', 'xdesc': 'Carrasco'},

{'east': '-54', 'north': '-34', 'south': '-35', 'west': '-55', 'xdesc': 'Punta del Este'},


#{'east': '-61', 'north': '-50', 'south': '-51', 'west': '-62', 'xdesc': 'Malvinas'},
#{'east': '-61', 'north': '-51', 'south': '-52', 'west': '-62', 'xdesc': 'Malvinas'},
#{'east': '-61', 'north': '-52', 'south': '-53', 'west': '-62', 'xdesc': 'Malvinas'},
#
#{'east': '-60', 'north': '-50', 'south': '-51', 'west': '-61', 'xdesc': 'Malvinas'},
#{'east': '-60', 'north': '-51', 'south': '-52', 'west': '-61', 'xdesc': 'Malvinas'},
#{'east': '-60', 'north': '-52', 'south': '-53', 'west': '-61', 'xdesc': 'Malvinas'},
#
#{'east': '-59', 'north': '-50', 'south': '-51', 'west': '-60', 'xdesc': 'Malvinas'},
#{'east': '-59', 'north': '-51', 'south': '-52', 'west': '-60', 'xdesc': 'Malvinas'},
#{'east': '-59', 'north': '-52', 'south': '-53', 'west': '-60', 'xdesc': 'Malvinas'},
#
#{'east': '-58', 'north': '-50', 'south': '-51', 'west': '-59', 'xdesc': 'Malvinas'},
#{'east': '-58', 'north': '-51', 'south': '-52', 'west': '-59', 'xdesc': 'Malvinas'},
#{'east': '-58', 'north': '-52', 'south': '-53', 'west': '-59', 'xdesc': 'Malvinas'},
#
#{'east': '-57', 'north': '-50', 'south': '-51', 'west': '-58', 'xdesc': 'Malvinas'},
#{'east': '-57', 'north': '-51', 'south': '-52', 'west': '-58', 'xdesc': 'Malvinas'},
#{'east': '-57', 'north': '-52', 'south': '-53', 'west': '-58', 'xdesc': 'Malvinas'},

#{'east': '87', 'north': '28', 'south': '27', 'west': '86', 'xdesc': 'Lukla'},
#{'east': '86', 'north': '28', 'south': '27', 'west': '85', 'xdesc': 'Katmandu'},

]

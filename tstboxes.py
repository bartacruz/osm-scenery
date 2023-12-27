import config
import get
layer = {
    'name':'tertiary',
    'line-type': 'Asphalt',
    'line-width': 5,
}
box = {'east': '-58', 'north': '-34', 'south': '-35', 'west': '-59', 'xdesc': 'Buenos Aires'}
filename = "data/%s.osm" % config.box2tile(box)
get.osm_to_shape(filename,layer)
#for box in config.boxes:
#    if int(box['south']) >= int(box['north']) or int(box['west']) >= int(box['east']):
#        print(box)

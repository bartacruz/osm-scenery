#!/usr/bin/python
import config 
import requests
import os
import shutil

api_url = "http://overpass-api.de/api/interpreter"
fixed_layer = False

def download_file_old(url, data, filename):
    with requests.post(url, data=data, stream=True) as r:
        with open(filename, 'w') as f:
            shutil.copyfileobj(r.raw.decode('utf-8'), f)

    return filename

def download_file(url, data, filename):
    # NOTE the stream=True parameter below
    with requests.post(url, data=data, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return filename



def get_osm(layer,bbox, filename):
    name = layer["name"]
    if layer.get('landuse',False):
        conf_file=open('conf/landuse.xml', 'r')
    else:
        conf_file=open('conf/%s.xml' % name, 'r')
    conf_data =conf_file.read()  
    conf_file.close()
    conf_data = conf_data.replace("{{bbox}}",bbox)
    conf_data = conf_data.replace("{{landuse}}",name)
    #r = requests.post(url = api_url, data = conf_data)
    filename = filename or 'data/%s.osm' % name
    download_file(api_url, conf_data, filename)
    #osm_data=open(filename, 'wb')
    #osm_data.write(r.text.encode('utf-8'))
    #osm_data.close()

def get_osm_tile(box):
    #bbox = 'e="%s" n="%s" s="%s" w="%s"' % (box['east'],box['north'],box['south'],box['west'])
    bbox = '%s,%s,%s,%s' % (box['east'],box['north'],box['south'],box['west'])
    template = '[out:xml];(node({{bbox}});<;);out meta;'
    conf_data = template.replace("{{bbox}}",bbox)
    filename = "data/%s.osm" % config.box2tile(box)
    print(filename, conf_data)
    download_file(api_url, conf_data, filename)


def osm_to_shape(filename,layer):
    name = layer.get('name')
    key = layer.get('key',None)
    external = layer.get('external',False)
    if key:
        with open('conf/%s.filter' % key) as f: line=f.read().replace('{{name}}',name).strip()
        shapefile="/vsistdin/"
    elif external:
        line=None
        shapefile = "data/%s.osm" % name
    else:
        with open('conf/%s.filter' % name) as f: line=f.read().strip()
        shapefile="/vsistdin/"
    filter_command='osmfilter %s %s' % (filename, line) 
    ogr_command='ogr2ogr  -overwrite -skipfailures -f "ESRI Shapefile" data/%s %s' % (name,shapefile)
    if external:
        command = ogr_command
    else:
        command = '%s | %s' % (filter_command, ogr_command,)
    print(command)
    os.system(command)

def to_shape(layer):    
    ogr_command='ogr2ogr -nlt MULTIPOLYGON -overwrite -skipfailures -f "ESRI Shapefile" data/%s  data/%s.osm' % (layer,layer,)
    os.system(ogr_command)

def decode(layer):
    if layer.get("external",False):
        shapefile = layer['name']
    else:
        shapefile = "multipolygons"
    name= layer['name']
    terrain_type = layer.get('terrain',False)
    if terrain_type:
        ogr_command='ogr-decode  --max-segment 500 --area-type %s work/%s data/%s/%s.dbf' % (terrain_type,name,name,shapefile)
        print(ogr_command)
        os.system(ogr_command)

    line_type = layer.get("line-type",False)
    if line_type:
        line_width = layer.get("line-width",5)
        ogr_command='ogr-decode  --max-segment 500 --line-width %s --area-type %s work/%s_line data/%s/%s.dbf' % (line_width, line_type,name,name,'lines')
        print(ogr_command)
        os.system(ogr_command)


def do_layer(layer,bbox):
    if not layer.get("external",False):
        if config.download_enabled:
            print("Fetching %s" % layer["name"])
            get_osm(layer,bbox)
        print("Shaping %s" % layer["name"])
        to_shape(layer['name'])
    print("Decoding %s" % layer["name"])
    decode(layer)

def process_box(box):
    bbox = 'e="%s" n="%s" s="%s" w="%s"' % (box['east'],box['north'],box['south'],box['west'])
    for layer in config.layers:
        if fixed_layer and layer["name"] is not fixed_layer:
            continue
        do_layer(layer,bbox)

if __name__ == "__main__":
    layer = {
        'name':'water',
        'terrain':'Lake',
        'line-type': 'Stream',
    }
    #box = {'east': '-70', 'north': '-40', 'south': '-45', 'west': '-75', 'xdesc': 'Bariloche'} 
    box = {'east': '-71', 'north': '-41', 'south': '-42', 'west': '-72', 'xdesc': 'Bariloche'}
    bbox = 'e="%s" n="%s" s="%s" w="%s"' % (box['east'],box['north'],box['south'],box['west'])
    get_osm(layer,bbox,'data/water3-barilo.osm')
    #for box in config.boxes:
    #    get_osm_tile(box)
        #process_box(box)


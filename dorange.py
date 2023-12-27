#!/usr/bin/python
import config 
import apts
import get
import construct
import osm2city
import logging
import math
import os

FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(filename="/opt/log/progress.log", level=logging.INFO, format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S')

    
def make_box(box):
    apts.do_apts(box)
    logging.info("Starting terrain for box %s " % box)
    #filename = "data/range.osm"
    filename = "data/%s.osm" % config.box2tile(box)
    if config.download_enabled:
        osm2city.get_data(box,filename)
        #get.get_osm_tile(box)
    for layer in config.layers:
        if not layer.get("external",False):
            get.osm_to_shape(filename,layer)
            get.decode(layer)
    construct.process_box(box)
    source = os.path.join('output/Terrain',config.box2dir(box),config.box2tile(box))
    inter = os.path.join('/var/www/scenery/','Terrain',config.box2dir(box))
    dest = os.path.join(inter, config.box2tile(box))
    cmd1 = "/bin/rm -Rf %s" %  dest
    print("Ejecutando",cmd1)
    os.system(cmd1)
    cmd2 = "mkdir -p %s && cp -a %s %s" % (inter, source,dest,)
    print("Ejecutando",cmd2)
    os.system(cmd2)
    logging.info("Ended terrain for %s " % box.get('xdesc'))


    #{'east': '-58', 'north': '-34', 'south': '-35', 'west': '-59', 'xdesc': ' Buenos Aires'},

def make_range():
    east = -50
    west = -60
    south = -40
    north = -30
    e=w=s=n = None
    for lat in range(south,north+1):
        s=n
        n=lat
        e=None
        w=None
        for lon in range(west,east+1):
            w=e
            e=lon
            if s and w:
                box = {'east': e, 'north': n, 'south': s, 'west': w, 'xdesc': 'range'}
                print(box)
                make_box(box)

if __name__ == "__main__":
    for box in config.boxes:
        make_box(box)


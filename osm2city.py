#!/usr/bin/python
import config
import os
import logging

FORMAT = "%(asctime)-15s %(message)s"
logging.basicConfig(filename="/opt/log/progress.log", level=logging.INFO, format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S')

ini_file='osmcity.ini'
osmosis='/home/julio/src/osmosis/bin/osmosis'
db = 'osm_auto'
user = 'flightgear'
password='!!********'

def make_ini(box):
    f = open('conf/%s' % ini_file)
    ini = f.read()
    f.close()
    ini += 'BOUNDARY_WEST=%s\n' % box['west']
    ini += 'BOUNDARY_EAST=%s\n' % box['east']
    ini += 'BOUNDARY_SOUTH=%s\n' % box['south']
    ini += 'BOUNDARY_NORTH=%s\n' % box['north']
    f = open('city/%s' % ini_file,'w')
    f.write(ini)
    f.close()

def get_data(box, filename):
    print(box,filename,)
    command='wget "http://overpass-api.de/api/map?bbox=%s,%s,%s,%s" -O %s' % (box['west'],box['south'],box['east'],box['north'],filename)
    os.system(command)

def clean_db():
    command='%s --truncate-pgsql database=%s user=%s password="%s"' % (osmosis,db,user,password)
    os.system(command)

def import_data(filename):
    command='%s --read-xml file=%s --log-progress --write-pgsql database=%s user=%s password="%s"' % (osmosis,filename,db,user,password)
    print(command)
    os.system(command)

def run(box):
    command = 'cd city;  ./do_city.sh'
    command += ' *%s_%s_%s_%s' % (box['west'],box['south'], box['east'], box['north'])
    os.system(command)
def move_data(box):
    for folder in ['Buildings','Details','Pylons','Roads']:
        dest_folder = 'Objects' if folder == 'Details' else folder
        source = os.path.join('output',folder,config.box2dir(box),config.box2tile(box))
        inter = os.path.join('/var/www/scenery/', dest_folder, config.box2dir(box))
        dest = os.path.join(inter, config.box2tile(box))
        cmd1 = "/bin/rm -Rf %s" %  dest
        print("Ejecutando",cmd1)
        os.system(cmd1)
        cmd2 = "mkdir -p %s && cp -a %s %s" % (inter, source, dest,)
        print("Ejecutando",cmd2)
        os.system(cmd2)
def process_box(box):
    logging.info("Starting osm2city for %s " % box.get('xdesc'))
    make_ini(box)
    filename='data/%s.osm' % config.box2tile(box)
    clean_db()
    import_data(filename)
    run(box)
    move_data(box)
    logging.info("Ended osm2city for %s" % box.get('xdesc'))

if __name__ == "__main__":
    for box in config.boxes:
        #move_data(box)
        #filename='data/%s.osm' % config.box2tile(box)
        #get_data(box, filename)
        process_box(box)



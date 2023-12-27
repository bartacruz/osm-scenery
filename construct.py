#!/usr/bin/python

import config
import os

tile = False
tile_id=1822362

priorities='/home/julio/src/scenery/auto/priorities.txt'
work_dir='/home/julio/src/scenery/auto/work'
output_dir='%s/Terrain' % config.output_dir
dem_dir='/home/julio/src/scenery/auto/work/SRTM-3'

base_terrain=['AirportObj', 'Landmass', 'AirportArea', 'SRTM-3', 'water2', 'Stream']
base_command='tg-construct --ignore-landmass --threads --priorities=%s --work-dir=%s --output-dir=%s' % (priorities,work_dir,output_dir)

def process_tile(tile):
    commands = []
    commands.append(base_command)
    commands.append('--tile-id=%s' % tile_id)
    return _process(commands)

def process_box(box):
    commands = []
    commands.append(base_command)
    commands.append('--min-lat=%s --max-lat=%s --min-lon=%s --max-lon=%s' % (box['south'],box['north'],box['west'],box['east']))
    return _process(commands)

def _process(commands):
    terrain = base_terrain + config.get_names()
    terrains = ["%s/%s" % (work_dir,x) for x in terrain]
    commands.append(" ".join(terrain))
    command= " ".join(commands)
    #print command
    os.system(command)

if __name__ == "__main__":
    if tile:
        process_tile(tile)
    else:
        for box in config.boxes:
            #print box
            process_box(box)

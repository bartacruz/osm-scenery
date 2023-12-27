#!/usr/bin/python

import config
import os

tile = False
tile_id=1986003

icao = False

aptfile='/home/julio/src/scenery/auto/apt.dat'
work_dir='/home/julio/src/scenery/auto/work'
dem_dir='/home/julio/src/scenery/auto/work/SRTM-3'

def do_apts(box=None):
    command = 'genapts850 --threads --input=%s --work=%s --dem-path=%s ' % (aptfile,work_dir,dem_dir)

    if tile:
        command = command + '--tile-id=%s' % tile_id
        os.system(command)
    elif icao:
        command = command + '--airport=%s' % icao
        os.system(command)
    elif box:
        comm = command+('--min-lat=%s --max-lat=%s --min-lon=%s --max-lon=%s' % (box['south'],box['north'],box['west'],box['east']))
        print(comm)
        os.system(comm)

if __name__ == "__main__":
    if icao:
        do_apts()
    else:
        for box in config.boxes:
            do_apts(box)



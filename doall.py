#!/usr/bin/python
import config 
import .apts
import .get
import .construct
import .osm2city

if __name__ == "__main__":
    for box in config.boxes:
        apts.process_box(box)
        get.process_box(box)
        construct.process_box(box)
        osm2city.process_box(box)
